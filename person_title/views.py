# Create your views here.
from rest_framework import viewsets

from .serializers import PersonTitleSerializer
from .models import PersonTitle
from rest_framework.permissions import IsAuthenticated


class PersonTitleViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PersonTitle.objects.all()
    serializer_class = PersonTitleSerializer
