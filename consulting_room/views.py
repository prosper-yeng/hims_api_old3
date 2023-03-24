# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ConsultingRoomSerializer
from .models import ConsultingRoom


class ConsultingRoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ConsultingRoom.objects.all()
    serializer_class = ConsultingRoomSerializer
