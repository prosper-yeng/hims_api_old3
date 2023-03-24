from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from person.models import LoggedInUserDevices
from person.serializers import LoggedInUserDevicesSerializer

class LoggedInUserDevicesReportViewSet(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoggedInUserDevicesSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = LoggedInUserDevices.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        user_id = request.query_params.get("user_id", None)
        is_active = request.query_params.get("is_active", None)
        ip_address = request.query_params.get("ip_address", None)

         # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_at__date=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_at__range=(start_date, end_date))

        # Query by user id
        if user_id is not None:
            queryset = queryset.filter(user__id=user_id)

        # Query by is active
        if is_active is not None:
            queryset = queryset.filter(is_active=True)

        # Query by ip address
        if ip_address is not None:
            queryset = queryset.filter(ip_address=ip_address)

        data = self.serializer_class(queryset, many=True).data
        return Response({
            "count":len(data),
            "data": data
        })