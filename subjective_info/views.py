from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import SubjectiveInfo
from .serializers import SubjectiveInfoSerializer


class SubjectiveInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SubjectiveInfo.objects.all()
    serializer_class = SubjectiveInfoSerializer