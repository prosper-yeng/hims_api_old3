from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import InterventionImplementation
from .serializers import InterventionImplementationSerializer, InterventionImplementationDetailsSerializer


class InterventionImplementationViewSet(viewsets.ModelViewSet):
    queryset = InterventionImplementation.objects.all()
    serializer_class = InterventionImplementationSerializer
    #permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": InterventionImplementationDetailsSerializer,
        "list": InterventionImplementationDetailsSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(InterventionImplementationViewSet, self).get_serializer_class()
