import jwt
from django.shortcuts import render, redirect

from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    GroupSerializer,
    GroupUpdateStatusSerializer,
    CombinedGroupPermissionSerializer,
)
from .models import Group
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    action_serializers = {
        "retrieve": CombinedGroupPermissionSerializer,
        "list": CombinedGroupPermissionSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(GroupViewSet, self).get_serializer_class()


class GroupView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        try:
            # payload = jwt.decode(token, 'secret', algorithm=['HS256'])
            query_data = Group.objects.filter(status="active")
            serializer = GroupSerializer(query_data, many=True)

            return Response(serializer.data)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unknown Error!")

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "group_detail.html"

    def get(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        serializer = GroupSerializer(group)
        return Response({"serializer": serializer, "group": group})

    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        serializer = GroupSerializer(group, data=request.data)
        if not serializer.is_valid():
            return Response({"serializer": serializer, "group": group})
        serializer.save()
        return redirect("group-list.html")


class UpdateGroup(UpdateAPIView):
    """This endpoint allows for updating a specific group by passing in the id of the user to update"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UpdateGroupStatus(UpdateAPIView):
    """This endpoint allows for updating the status of a  group by passing in the id of the user to update"""

    queryset = Group.objects.all()
    serializer_class = GroupUpdateStatusSerializer


class CombinedGroupPermissionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        query_data = Group.objects.all()
        serialized = CombinedGroupPermissionSerializer(query_data, many=True)
        return Response(serialized.data)
