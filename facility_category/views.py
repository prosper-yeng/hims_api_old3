# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView


from .serializers import FacilityCategorySerializer
from .models import FacilityCategory
from rest_framework.permissions import IsAuthenticated


class FacilityCategoryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FacilityCategory.objects.all()
    serializer_class = FacilityCategorySerializer
