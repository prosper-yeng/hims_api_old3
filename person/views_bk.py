# Create your views here.
import jwt, datetime

from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication,
)
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    UserSerializer,
    PatientSerializer,
    StaffSerializer,
    LogInSerializer,
)
from .models import Patient, Staff


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


class PatientViewSet(APIView):  # (viewsets.ModelViewSet):
    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        try:
            # payload = jwt.decode(token, 'secret', algorithm=['HS256'])
            query_data = Patient.objects.all()
            serializer = PatientSerializer(query_data)

            return Response(serializer.data)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")

    # # authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication)
    #
    # # permission_classes = (IsAuthenticated,)
    # queryset = Patient.objects.all()
    # permission = [
    #     permissions.IsAuthenticated
    # ]
    #
    # # def destroy(self, request, *args, **kwargs):
    # #     patient = request.user  # deleting user
    # #     user = patient.user
    # #     patient.delete()
    # #     user.delete()
    # #     return super(PatientViewSet, self).destroy(request, *args, **kwargs)
    #
    # serializer_class = PatientSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StaffSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, "secret", algorithm="HS256").decode("utf-8")

        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}
        return response


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


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "success"}
        return response
