from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from person.models import Patient
from .models import DailyAttendanceModel
from .serializers import DailyAttendanceSerializer, CombinedPatientAttendanceSerializer


class DailyAttendanceViewset(viewsets.ModelViewSet):
    queryset = DailyAttendanceModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DailyAttendanceSerializer


class CombinedPatientAttendanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = DailyAttendanceModel.objects.all()
        serialized = CombinedPatientAttendanceSerializer(query_data, many=True)
        return Response(serialized.data)
