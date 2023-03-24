from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import NursesNote
from .serializers import NursesNoteSerializer, NursesNoteDetailsSerializer


class NursesNoteViewSet(viewsets.ModelViewSet):
    queryset = NursesNote.objects.all()
    serializer_class = NursesNoteSerializer
    permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": NursesNoteDetailsSerializer,
        "list": NursesNoteDetailsSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(NursesNoteViewSet, self).get_serializer_class()
