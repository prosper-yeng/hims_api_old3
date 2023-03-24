from rest_framework import serializers

from choice.views import StatusChoice
from service.models import Service
from service_charge.models import ServiceCharge
from service_bill.models import ServiceBill

# from work_flow.models import WorkFlow
from .models import Transaction
from transaction_log.models import TransactionLog


class TransactionSerializer(serializers.ModelSerializer):
    service_type = serializers.CharField(required=False)
    service_name = serializers.CharField(source="service", required=False)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "service",
            "patient",
            "access_level",
            "transaction_date",
            "assigned_group",
            "assigned_user",
            "note",
            "created_by",
            "status",
            "service_type",
            "service_name",
        ]
        read_only_fields = ("id", "status")

    def create(self, validated_data):
        service = validated_data.get("service", None)
        if service:
            service_type = Service.objects.get(id=service.id).service_type
            transaction = Transaction.objects.create(
                service_type=service_type, **validated_data
            )

            # add the transaction log
            result = TransactionLog.objects.create(
                transaction=transaction,
                access_level=transaction.access_level,
                action="CREATED",
                note=transaction.note,
                created_by=transaction.created_by,
            )
            result.save()

            # add the bill if any
            service_charge = ServiceCharge.objects.filter(
                service=transaction.service
            ).first()
            if service_charge:
                service_charge = ServiceBill.objects.create(
                    transaction=transaction,
                    service=transaction.service,
                    amount=service_charge.amount,
                    currency_type=service_charge.currency_type,
                    created_by=transaction.created_by,
                )

            return transaction

    def update(self, instance, validated_data):
        instance.service = validated_data.get("service", instance.transaction_type)
        instance.patient = validated_data.get("patient", instance.patient)
        instance.access_level = validated_data.get(
            "access_level", instance.access_level
        )
        instance.assigned_group = validated_data.get(
            "assigned_group", instance.assigned_group
        )
        instance.assigned_user = validated_data.get(
            "assigned_user", instance.assigned_user
        )
        instance.note = validated_data.get("note", instance.note)
        instance.status = validated_data.get("status", instance.note)
        instance.save()

        result = TransactionLog.objects.create(
            transaction=instance,
            access_level=instance.access_level,
            action="UPDATED",
            note=instance.note,
            created_by=instance.created_by,
        )
        result.save()

        return instance


class TransactionSubmitSerializer(serializers.ModelSerializer):
    action = serializers.CharField(required=False)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "modified_by",
            "status",
            "action",
        ]

    def update(self, instance, validated_data):
        # transaction_data = Transaction.objects.filter(id=instance.id).first()

        # workflow = WorkFlow.objects.filter(service_id=instance.service_id,
        #                                    access_level__gt=instance.access_level).first()
        # if workflow:
        #     instance.access_level = workflow.access_level
        #     instance.assigned_group = workflow.group

        # else:
        instance.status = StatusChoice.CLOSED

        instance.save()

        result = TransactionLog.objects.create(
            transaction=instance,
            access_level=instance.access_level,
            action=validated_data.get("action", None),
            created_by=validated_data.get("modified_by", None),
        )
        result.save()

        return instance


class MyTasksSerializer(serializers.ModelSerializer):
    patient_title = serializers.CharField(source="patient.title.text", required=False)
    patient_name = serializers.CharField(source="patient", required=False)
    patient_gender = serializers.CharField(
        source="patient.user.gender.text", required=False
    )
    patient_dob = serializers.CharField(
        source="patient.user.date_of_birth", required=False
    )
    service_name = serializers.CharField(source="service", required=False)
    resident_address = serializers.CharField(
        source="patient.resident_address", required=False
    )
    email = serializers.CharField(source="patient.user.email", required=False)
    primary_phone = serializers.CharField(
        source="patient.user.primary_phone", required=False
    )
    secondary_phone = serializers.CharField(
        source="patient.user.secondary_phone", required=False
    )
    assigned_group_name = serializers.CharField(source="assigned_group", required=False)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "service",
            "service_name",
            "patient",
            "patient_title",
            "patient_name",
            "patient_gender",
            "patient_dob",
            "resident_address",
            "email",
            "primary_phone",
            "secondary_phone",
            "access_level",
            "transaction_date",
            "assigned_group",
            "assigned_group_name",
            "assigned_user",
            "note",
            "created_by",
            "status",
        ]
