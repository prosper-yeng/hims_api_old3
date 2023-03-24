from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import BedAllocation
from .serializers import BedAllocationSerializer, BedAllocationDetailsSerializer


class BedAllocationViewSet(viewsets.ModelViewSet):
    queryset = BedAllocation.objects.all()
    serializer_class = BedAllocationSerializer
    permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": BedAllocationDetailsSerializer,
        "list": BedAllocationDetailsSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(BedAllocationViewSet, self).get_serializer_class()
