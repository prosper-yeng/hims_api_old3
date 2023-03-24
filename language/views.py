from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LanguageSerializer
from .models import Language
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer


class LanguageViewset(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = LanguageSerializer
