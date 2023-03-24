from django.http import request
from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect


class StatusChoice(models.TextChoices):
    CREATED = "created", "Created"
    APPROVED = "approved", "Approved"
    ACTIVE = "active", "Active"
    DEACTIVATE = "deactivate", "Deactivate"
    SUSPENDED = "suspended", "Suspended"
    DELETE = "delete", "Delete"
    CLOSED = "closed", "Closed"
    REGISTERED = "registered", "Registered"
    VITAL = "vital done", "Vital Done"
    DIAGNOSED = "diagnosed", "Diagnosed"
    BILLED = "billed", "Billed"
    LAB = "pending lab", "Pending Lab"
    PHARMACY = "pending pharmacy", "Pending Pharmacy"


class PersonTypeChoice(models.TextChoices):
    ADMIN = "admin", "Administrator"
    DOCTOR = "doctor", "Doctor"
    NURSE = "nurse", "Nurse"
    PATIENT = "patient", "Patient"


class GenderChoice(models.TextChoices):
    FEMALE = "female", "Female"
    MALE = "male", "Male"


class MaritalChoice(models.TextChoices):
    SINGLE = "single", "Single"
    MARRIED = "married", "Married"


class ReligionChoice(models.TextChoices):
    CHRISTIAN = "christian", "Christian"
    MUSLIM = "muslim", "Muslim"
    TRADITION = "traditional", "Traditional"


class RelativeChoice(models.TextChoices):
    FATHER = "father", "Father"
    MOTHER = "mother", "Mother"
    BROTHER = "Brother", "Brother"
    SISTER = "sister", "Sister"
    UNCLE = "uncle", "Uncle"
    FRIEND = "friend", "Friend"
    AUNT = "aunt", "Aunt"


class SponsorTypeChoice(models.TextChoices):
    SELF = "self", "Self"
    RELATIVE = "Relative", "Relative"
    NHIS = "nhis", "NHIS"


class OccupationChoice(models.TextChoices):
    FARMER = "farmer", "Farmer"
    TEACHER = "teacher", "Teacher"


class TitleChoice(models.TextChoices):
    MR = "mr", "Mr"
    MISS = "miss", "Miss"
    MRS = "mrs", "Mrs"


class LanguageChoice(models.TextChoices):
    DAGAARE = "dagaare", "Dagaare"
    TWI = "twi", "Twi"
    ENGLISH = "english", "English"


class EducationLevelChoice(models.TextChoices):
    PRIMARY = "primary", "Primary"
    SENIOR_HIGH = "senior_high", "Senior High"
    JUNIOR_HIGH = "junior_high", "Junior High"
    NOT_EDUCATED = "not_educated", "Not Educated"
    FIRST_DEGREE = "first_degree", "First Degree"
    SECOND_DEGREE = "second_degree", "Second Degree"
    PHD = "phd", "PhD"


class FacilityCategoryChoice(models.TextChoices):
    CLINIC = "clinic", "Clinic"
    MATERNITY = "maternity", "Maternity"
    HEALTH_CENTER = "health_center", "Health Center"
    HOSPITAL = "hospital", "Hospital"


def visitor_ip_address(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class AddressTypeChoice(models.TextChoices):
    HOME = "home", "Home"
    WORK = "work", "Work"


class UrgencyTypeChoice(models.TextChoices):
    URGENCY = "urgent", "URGENT"
    NORMAL = "normal", "NORMAL"


class FastingTypeChoice(models.TextChoices):
    FASTING = "fasting", "FASTING"
    NONFASTING = "non-fasting", "NON-FASTING"


class QuantityUnitTypeChoice(models.TextChoices):
    BOX = "box", "BOX"
    PACKAGE = "package", "PACKAGE"
    STRIP = "strip", "STRIP"
    BASE_UNIT = "base_unit", "BASE_UNIT"


class MedicationTypeChoice(models.TextChoices):
    TABLET = "tablet", "TABLET"
    CAPSULE = "capsule", "CAPSULE"
    SYRUP_SUSPENSION = "syrup_suspension", "SYRUP_SUSPENSION"
    INJECTION = "injection", "INJECTION"
    CREAM_OINTMENT = "cream_ointment", "CREAM_OINTMENT"
    DROP = "drop", "DROP"
    GUM = "gum", "GUM"
    SACHET = "sachet", "SACHET"


class DurationUnitChoice(models.TextChoices):
    DAY = "day", "DAY"
    WEEK = "week", "WEEK"
    MONTH = "month", "MONTH"
