from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User, Group

from facility.serializers import FacilitySerializer
from groups.serializers import GroupSerializer
from marital_status.serializers import MaritalStatusSerializer
from occupation.serializers import OccupationSerializer
from person_title.serializers import PersonTitleSerializer
from religion.serializers import ReligionSerializer
from .models import LoggedInUserDevices

from .models import Patient, Staff



class UserSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source="group.name", required=False)
    gender_name = serializers.CharField(source="gender.text", required=False)
    nationality_name = serializers.CharField(source="nationality.text", required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "facility",
            "group",
            "group_name",
            "username",
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "gender",
            "gender_name",
            "email",
            "nationality",
            "nationality_name",
            "national_id",
            "primary_phone",
            "secondary_phone",
            "photo_url",
            "password",
            "is_active",
            "created_by",
            "status",
        )

        read_only_fields = ("id",)

    def create(self, validated_data):
        password = validated_data.get("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        User.objects.filter(id=instance.id).update(**validated_data)
        instance = User.objects.get(id=instance.id)

        if password is not None:
            instance.set_password(password)

        instance.save()

        # return instance

        return instance

    # password = validated_data.pop ( 'password', None )

    # for (key, value) in validated_data.items ():
    # setattr ( instance, key, value )

    # if password is not None:
    # instance.set_password ( password )

    # instance.save ()

    # return instance


class LoggedInUserDevicesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta: 
        model = LoggedInUserDevices
        fields = "__all__"


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "old_password",
            "password",
            "password2",
            "created_by",
            "status",
        )
        read_only_fields = ("id",)

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])

        instance.save()
        return instance


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    title_name = serializers.CharField(source="person_title.name", required=False)
    occupation_name = serializers.CharField(source="occupation.name", required=False)
    marital_status_name = serializers.CharField(
        source="marital_status.name", required=False
    )
    religion_name = serializers.CharField(source="religion.name", required=False)

    facility_name = serializers.CharField(source="user.facility", required=False)
    email = serializers.CharField(source="user.email", required=False)

    class Meta:
        model = Patient
        fields = (
            "id",
            "title",
            "marital_status",
            "occupation",
            "religion",
            "full_name",
            "title_name",
            "occupation_name",
            "marital_status_name",
            "religion_name",
            "facility_name",
            "email",
            "created_by",
            "created_on",
            "status",
            "is_deleted",
            "user",
        )

        read_only_fields = ("id",)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        password = user_data.get("password")
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        patient = Patient.objects.create(user=user, **validated_data)

        return patient

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        instance.title = validated_data.get("title", instance.title)
        instance.marital_status = validated_data.get(
            "marital_status", instance.marital_status
        )
        instance.occupation = validated_data.get("occupation", instance.occupation)
        instance.religion = validated_data.get("religion", instance.religion)
        instance.save()

        uid = instance.user_id

        user = User.objects.get(id=uid)

        user.facility = user_data.get("facility", user.facility)
        user.group = user_data.get("group", user.group)
        user.first_name = user_data.get("first_name", user.first_name)
        user.middle_name = user_data.get("middle_name", user.middle_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.date_of_birth = user_data.get("date_of_birth", user.date_of_birth)
        user.gender = user_data.get("gender", user.gender)
        user.email = user_data.get("email", user.email)
        user.nationality = user_data.get("nationality", user.nationality)
        user.national_id = user_data.get("national_id", user.national_id)
        user.primary_phone = user_data.get("primary_phone", user.primary_phone)
        user.secondary_phone = user_data.get("secondary_phone", user.secondary_phone)
        user.photo_url = user_data.get("photo_url", user.photo_url)
        user.password = user_data.get("password", user.password)

        user.save()

        return instance


class ExistingUserAsPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            "id",
            "user",
            "title",
            "marital_status",
            "occupation",
            "religion",
        )

        read_only_fields = ("id",)


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    facility = serializers.CharField(source="user.facility.name", required=False)
    email = serializers.CharField(source="user.email", required=False)
    first_name = serializers.CharField(source="user.first_name", required=False)
    middle_name = serializers.CharField(source="user.middle_name", required=False)
    last_name = serializers.CharField(source="user.last_name", required=False)
    occupation_name = serializers.CharField(source="occupation.name", required=False)
    marital_status_name = serializers.CharField(
        source="marital_status.name", required=False
    )
    religion_name = serializers.CharField(source="religion.name", required=False)

    class Meta:
        model = Staff
        fields = (
            "id",
            "facility",
            "title",
            "occupation",
            "marital_status",
            "religion",
            "first_name",
            "middle_name",
            "last_name",
            "full_name",
            "email",
            "occupation_name",
            "marital_status_name",
            "religion_name",
            "user",
        )

        read_only_fields = ("id",)

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        password = user_data.get("password")
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        staff = Staff.objects.create(user=user, **validated_data)

        return staff

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        instance.title = validated_data.get("title", instance.title)
        instance.marital_status = validated_data.get(
            "marital_status", instance.marital_status
        )
        instance.occupation = validated_data.get("occupation", instance.occupation)
        instance.religion = validated_data.get("religion", instance.religion)
        instance.save()

        uid = instance.user_id

        user = User.objects.get(id=uid)

        user.facility = user_data.get("facility", user.facility)
        user.group = user_data.get("group", user.group)
        user.first_name = user_data.get("first_name", user.first_name)
        user.middle_name = user_data.get("middle_name", user.middle_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.date_of_birth = user_data.get("date_of_birth", user.date_of_birth)
        user.gender = user_data.get("gender", user.gender)
        user.email = user_data.get("email", user.email)
        user.nationality = user_data.get("nationality", user.nationality)
        user.national_id = user_data.get("national_id", user.national_id)
        user.primary_phone = user_data.get("primary_phone", user.primary_phone)
        user.secondary_phone = user_data.get("secondary_phone", user.secondary_phone)
        user.photo_url = user_data.get("photo_url", user.photo_url)
        user.password = user_data.get("password", user.password)

        user.save()

        return instance


class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "default_pwd_changed", "username", "email", "password"]
        extra_kwargs = {
            "default_pwd": {"write_only": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        # pref_language = validated_data.pop('pref_language', None )
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            # instance.save ( pref_language )
            instance.save()
            return instance


class CombinedPatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    marital_status = MaritalStatusSerializer(many=False)
    title = PersonTitleSerializer(many=False)
    occupation = OccupationSerializer(many=False)
    religion = ReligionSerializer(many=False)

    class Meta:
        model = Patient
        fields = "__all__"


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField()


class PasswordResetSetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()

    def validate_password(self, password):
        # check for small letters
        if not any(char.islower() for char in password):
            raise serializers.ValidationError(
                {"message": "Weak password, Must contain at least one small letter"}
            )

        # check for capital letters
        if not any(char.isupper() for char in password):
            raise serializers.ValidationError(
                {"message": "Weak password, Must contain at least one capital letter"}
            )

        # check for numbers
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError(
                {"message": "Weak password, Must contain at least one number"}
            )

        # check for characters
        if not any(char.isascii() for char in password):
            raise serializers.ValidationError(
                {"message": "Weak password, Must contain at least one character"}
            )

        return password


class CombinedUserGroupSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=False)
    facility = FacilitySerializer(many=False)

    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username_phone_email = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True)


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=255)
