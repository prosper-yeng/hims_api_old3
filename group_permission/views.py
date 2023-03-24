import jwt
from django.shortcuts import render, redirect

from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import GroupPermissionSerializer
from groups.models import Group
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer


class GroupPermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupPermissionSerializer
