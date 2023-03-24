# Python/Django imports
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

# Local app imports
from .models import DoctorsNote
from .serializers import DoctorsNoteSerializer, DoctorsNoteDetailsSerializer


class DoctorsNoteViewSet(viewsets.ModelViewSet):
    queryset = DoctorsNote.objects.all()
    serializer_class = DoctorsNoteSerializer
    permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": DoctorsNoteDetailsSerializer,
        "list": DoctorsNoteDetailsSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(DoctorsNoteViewSet, self).get_serializer_class()
