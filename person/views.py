# Create your views here.
import django_filters
import jwt, datetime
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, authentication, generics
from django.contrib.auth.models import User
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication,
)
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.conf import settings
from .serializers import (
    UserSerializer,
    PatientSerializer,
    StaffSerializer,
    LogInSerializer,
    CombinedPatientSerializer,
    ChangePasswordSerializer,
    CombinedUserGroupSerializer,
    ExistingUserAsPatientSerializer,
    PasswordResetSerializer,
    PasswordResetSetPasswordSerializer,
    LoginSerializer,
    LogoutSerializer,
)
from .models import Patient, Staff, UserVerificationCode, LoggedInUserDevices
from groups.models import Group
from groups.serializers import CombinedGroupPermissionSerializer
from permission.serializers import PermissionSerializer
from .utils import send_forget_password_mail, get_user_ip_address
from .middlewares import UserMiddlewares


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class LogoutAllView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)


class PatientView(APIView):
    def get(self, request):
        # serializer_class = PatientSerializer
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        try:
            # payload = jwt.decode(token, 'secret', algorithm=['HS256'])
            query_data = Patient.objects.all()
            # serializer = PatientSerializer(query_data)
            serializer_class = PatientSerializer(query_data, many=True)
            return Response(serializer_class.data)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer


class ExistingUserAsPatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExistingUserAsPatientSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        validated_data = data.data
        set_active = request.query_params.get("set_active", None)
        
        user = UserMiddlewares.get_user_by_email_phone_username(
            username_phone_email = validated_data["username_phone_email"], 
            password = validated_data["password"]
        )
       
        try:
            if user:
                # Authenticate device logins
                auth_device_logins = LoggedInUserDevices.objects.filter(
                    user=user,
                    ip_address=get_user_ip_address(request),
                    browser=request.user_agent.browser.family,
                    os=request.user_agent.os,
                    is_active=True,
                )
                ## ALLOW CASE:
                #  - check : if same device
                #  - check :e if not device and no device for user
                if (auth_device_logins.exists()) or (
                    not auth_device_logins.exists()
                    and (
                        set_active
                        or not LoggedInUserDevices.objects.filter(
                            user=user, is_active=True
                        ).exists()
                    )
                ):
                    # clear all previous logins
                    LoggedInUserDevices.objects.filter(
                        user=user, is_active=True
                    ).update(is_active=False)
                    # Create new login
                    LoggedInUserDevices.objects.create(
                        user=user,
                        ip_address=get_user_ip_address(request),
                        browser=request.user_agent.browser.family,
                        os=request.user_agent.os,
                    )
                ## DENY CASE:
                #  -  check : if not device and other active logged in device
                elif (
                    not auth_device_logins.exists()
                    and LoggedInUserDevices.objects.filter(
                        user=user, is_active=True
                    ).exists()
                ):
                    return Response(
                        {
                            "message": "You can login on a single device and browser at a time"
                        },
                        405,
                    )

                else:
                    return Response({"message": "Not Allowed"}, 405)
                
                # Generate token
                token = RefreshToken.for_user(user)
                user_data = UserSerializer(user).data
                del user_data["password"]
                # Query user group
                group = Group.objects.get(id=user.group.id)
                # Return response
                return Response(
                    {
                        "access_token": str(token.access_token),
                        "refresh_token": str(token),
                        "user": user_data,
                        "group": CombinedGroupPermissionSerializer(group).data,
                        "permissions": PermissionSerializer(group.permissions, many=True).data
                    }
                )
            else:
                return Response({
                    {
                    "message": "Invalid credentials provided, please check and try again. Note that both fields may be case-sensitive"
                },
                404
                })
        except Exception as e:
            return Response(
                {
                    "message": str(e)
                },
                500,
            )


class LogoutView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LogoutSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        validated_data = data.data
        try:
            # close active device
            LoggedInUserDevices.objects.filter(
                ip_address=get_user_ip_address(request), is_active=True
            ).update(is_active=False)

            # Blacklist token
            token = RefreshToken(validated_data["refresh_token"])
            token.blacklist()
            return Response("Successful Logout", 200)
        except Exception as e:
            return Response(str(e), 400)


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        try:
            payload = jwt.decode(token, "secret", algorithm=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")

        user = User.objects.filter(id=payload["id"]).first()
        serializer = LogInSerializer(user)
        return Response(serializer.data)


class CombinedPatientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Patient.objects.all()
        serialized = CombinedPatientSerializer(query_data, many=True)
        return Response(serialized.data)


class PatientSearchView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        "user__first_name",
        "user__last_name",
        "user__date_of_birth",
        "user__primary_phone",
        "id",
        "user__national_id",
    ]


class ChangePasswordView(generics.UpdateAPIView):
    # permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer


class CombinedUserGroupView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = User.objects.all()
        serialized = CombinedUserGroupSerializer(query_data, many=True)
        return Response(serialized.data)


class PasswordResetRequestLinkView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        validated_data = data.data

        if User.objects.filter(email=validated_data["email"]).exists():
            # Get user
            user = User.objects.get(email=validated_data["email"])
            # Clear all old verification codes if exist
            old_verify_codes = UserVerificationCode.objects.filter(user=user)
            if old_verify_codes.exists():
                old_verify_codes.delete()
            # Generate verification code
            user_code = UserVerificationCode.objects.create(user=user)
            # Send verification code
            send_forget_password_mail(
                f"{settings.HOST_DOMAIN}api/password-reset/verify/{user_code.code}",
                user,
            )

            return Response(
                {"message": "Password reset link has been sent to your mail"}
            )
        return Response({"message": "User email does not exist"}, 404)


class PasswordResetView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordResetSetPasswordSerializer

    def get(self, request, token):
        verify_code = get_object_or_404(UserVerificationCode, code=token)
        if verify_code and not verify_code.is_expired():
            return Response({"message": "Code valid"})
        return Response({"message": "Invalid code"}, 404)

    def post(self, request, token):
        # Get verification code obj
        verify_code = get_object_or_404(UserVerificationCode, code=token)
        if verify_code and not verify_code.is_expired():
            data = self.serializer_class(data=request.data)
            data.is_valid(raise_exception=True)
            validated_data = data.data

            user = User.objects.get(email=verify_code.user.email)
            user.set_password(validated_data["password"])
            user.save()
            verify_code.delete()
            return Response({"message": "Password reset successful"})
        return Response({"message": "Invalid or expired code provided"}, 400)
