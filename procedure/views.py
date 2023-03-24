# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ProcedureSerializer
from .models import Procedure


class ProcedureViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
