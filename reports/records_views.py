from rest_framework import generics
from django.db.models import Sum

# from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from person.models import Patient
from person.serializers import PatientSerializer

from daily_attendance.models import DailyAttendanceModel
from daily_attendance.serializers import CombinedPatientAttendanceSerializer

from payment.models import Payment
from payment_by_sponsor.models import PaymentBySponsor
from payment_individual.models import PaymentIndividual
from payment.serializers import PaymentSerializer
from payment_by_sponsor.serializers import PaymentBySponsorSerializer
from payment_individual.serializers import PaymentIndividualSerializer

from sponsor_patient.models import SponsorPatient
from sponsor_patient.serializers import SponsorPatientDetailSerializer


class PatientListViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Patient.objects.filter(user__group__name="PATIENTS").select_related(
            "user"
        )
        date        = request.query_params.get("date", None)
        start_date  = request.query_params.get("start_date", None)
        end_date    = request.query_params.get("end_date", None)
        first_name  = request.query_params.get("first_name", None)
        last_name   = request.query_params.get("last_name", None)
        phone       = request.query_params.get("phone", None)
        dob         = request.query_params.get("date_of_birth", None)

        try:
            # Query by single DATE
            if date is not None:
                queryset = queryset.filter(created_on__date=date)

            # Query by DATE range
            if start_date is not None and end_date is not None:
                queryset = queryset.filter(created_on__range=(start_date, end_date))

            # Query by FIRST_NAME
            if first_name is not None:
                queryset = queryset.filter(user__first_name=first_name)

            # Query by LAST_NAME
            if last_name is not None:
                queryset = queryset.filter(user__last_name=last_name)

            # Query by PHONE
            if phone is not None:
                queryset = queryset.filter(user__primary_phone=phone)

            # Query by DOB
            if dob:
                queryset = queryset.filter(user__date_of_birth=dob)

        except:
            pass

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)


class AttendanceTrendViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CombinedPatientAttendanceSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = DailyAttendanceModel.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)


class RegistrationFeesViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer
    http_method_names = ["get"]

    def get(self, request):
        # Declare return data dict
        data = {}

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        individual = request.query_params.get("individual", None)
        sponsor = request.query_params.get("sponsor", None)

        # Query if Individual
        if individual is not None or (individual is None and sponsor is None):
            data["payment_individual"] = {}
            # Get total amount
            data["payment_individual"][
                "total_amount_paid"
            ] = PaymentIndividual.objects.aggregate(Sum("amount_paid"))[
                "amount_paid__sum"
            ]
            # Get queryset
            queryset = PaymentIndividual.objects.all()

            # Query by single DATE
            if date is not None:
                queryset = queryset.filter(created_on__date=date)

            # Query by DATE range
            if start_date is not None and end_date is not None:
                queryset = queryset.filter(created_on__range=(start_date, end_date))
            
            queryset_data = PaymentIndividualSerializer(queryset, many=True).data
            data["payment_individual"]["data"] = queryset_data

        # Query if Sponsor
        if sponsor is not None or (individual is None and sponsor is None):
            data["payment_sponsor"] = {}
            # Get total amount
            data["payment_sponsor"][
                "total_amount_paid"
            ] = PaymentBySponsor.objects.aggregate(Sum("amount_paid"))[
                "amount_paid__sum"
            ]
            # Get queryset
            queryset = PaymentBySponsor.objects.all()

            # Query by single DATE
            if date is not None:
                queryset = queryset.filter(created_on__date=date)

            # Query by DATE range
            if start_date is not None and end_date is not None:
                queryset = queryset.filter(created_on__range=(start_date, end_date))

            queryset_data = PaymentBySponsorSerializer(queryset, many=True).data
            data["payment_sponsor"]["data"] = queryset_data

        return Response(data)


class PatientsWithSponsorViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SponsorPatientDetailSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = SponsorPatient.objects.all().select_related(
            "patient", "sponsor", "created_by", "status"
        )

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        sponsor_name = request.query_params.get("sponsor_name", None)
        sponsor_email = request.query_params.get("sponsor_email", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Query by SPONSOR NAME
        if sponsor_name is not None:
            queryset = queryset.filter(sponsor__name=sponsor_name)

        # Query by SPONSOR EMAIL
        if sponsor_email is not None:
            queryset = queryset.filter(sponsor_email=sponsor_email)

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)
