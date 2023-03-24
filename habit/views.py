from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Habit
from .serializers import HabitSerializer, CombinedUserPatientHabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class CombinedUserPatientHabitView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Habit.objects.all()
        serialized = CombinedUserPatientHabitSerializer(query_data, many=True)
        return Response(serialized.data)
