import jwt
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from .serializers import PermissionSerializer
from .models import Permission

# from . import permissions


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PermissionSerializer
