# Create your views here.
from django.db.models import OuterRef, Exists
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

import vital_sign
from daily_attendance.models import DailyAttendanceModel
from vital_sign.models import VitalSign
from .serializers import ConsultationSerializer, CombinedConsultationVitalSignSerializer
from .models import Consultation
from rest_framework.response import Response
from rest_framework.views import APIView


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ConsultationSerializer


class ConsultationDetailViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]
    serializer_class = ConsultationSerializer

    def get_queryset(self):
        trans_id = self.request.query_params.get("trans_id", None)
        queryset = Consultation.objects.filter(transaction_id=trans_id)

        return queryset


"""
class VitalSignNotInConsultationView ( APIView ):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        #vital_id = self.request.query_params.get ( 'vital_id', None )
        #queryset = Consultation.objects.filter ( vital_sign_id=vital_id )

        #in_cons = Consultation.objects.filter ( vital_sign_id=OuterRef ( 'pk' ))
       # query_data=VitalSign.objects.annotate(has_consultation=Exists(in_cons)).filter(has_consultation=False)
        #query_data = Consultation.objects.select_related ( 'attenadance' )
        #query_data = Consultation.objects.select_related ( 'attendance' )
        #query_data=Consultation.objects.exclude (id__attendance)
        #attendance=Consultation.objects.filter(attendance_id__isnull=True)#
        query_data=Consultation.objects.select_related ( 'attendance' )

        #query_data= VitalSign.objects.all().exclude(id__in=Consultation.objects.all())
        #query_data = VitalSign.objects.all ()
        serialized = VitalSignNotInConsultationSerializer( query_data, many=True )
        return Response ( serialized.data )
"""


class CombinedConsultationVitalSignView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = queryset = Consultation.objects.all()
        serialized = CombinedConsultationVitalSignSerializer(query_data, many=True)
        return Response(serialized.data)
