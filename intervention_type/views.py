from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import InterventionType
from .serializers import InterventionTypeSerializer


class InterventionTypeViewSet ( viewsets.ModelViewSet ):
    queryset = InterventionType.objects.all ()
    serializer_class = InterventionTypeSerializer
    permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": InterventionTypeSerializer,
        "list": InterventionTypeSerializer,
    }

    def get_serializer_class(self):
        if hasattr ( self, "action_serializers" ):
            return self.action_serializers.get ( self.action, self.serializer_class )

        return super ( InterventionTypeViewSet, self ).get_serializer_class ()
