"""
Django settings for hims_api project.

"""
import os
from datetime import timedelta

# import django_on_heroku
# import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # loads the configs from .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    str(os.getenv("SECRET_KEY")), "8kqrbr5wd_np3h98*tr53p!*0ehrh^o%*9=fkn#5zn8@l&xrt6"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
HOST_DOMAIN = (
    "https://hims.pythonanywhere.com/" if not DEBUG else "http://127.0.0.1:8000/"
)   

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "dbbackup",
    "django_crontab",
    "django_filters",
    "django_user_agents",
    # Local apps
    "need_type",
    "patient_needs",
    "subjective_info",
    "physical_examination",
    "additional_data",
    "habit",
    "family_history",
    "social_history",
    "psychosocial_history",
    "immunizations",
    "obstetric_history",
    "patient_diagnosis",
    "patient_specific_goal",
    "intervention_type",
    "intervention_implementation",
    "evaluation",

    "reports",
    "patient_type",
    "radiology_category",
    "radiology_type",
    "radiology_procedure",
    "radiology_procedure_price",
    "radiology_procedure_price_sponsor",
    "radiology_procedure_request",
    "radiology_procedure_result",
    "radiology_material_used",
    "doctors_note",
    "patient_discharge",
    "patient_review",
    "procedure_care",
    "treatment_plan",
    "medication_administration",
    "nurses_note",
    "bed",
    "bed_allocation",
    "room",
    "inter_hospital_patient_transfer",
    "intra_hospital_patient_transfer",
    "ward",
    "ward_type",
    "vital_signs_monitoring",
    "admission",
    "facility",
    "select_item",
    "nation",
    "region",
    "district",
    "town",
    "groups",
    "permission",
    "language",
    "person",
    "address",
    "daily_attendance",
    "service_type",
    "patient_doctor",
    "transaction_type",
    "currency_type",
    "service_charge",
    "service",
    "service_bill",
    "vital_sign",
    "opd_bill_type",
    "opd_bill_patient",
    "lab_priority",
    "sample_type",
    "lab_test_type",
    "lab_test",
    "medication_type",
    "medication",
    "medication_bill",
    "site_type",
    "lab_test_site",
    "insurance_type",
    "prescription",
    "medication_bill_detail",
    "unit_of_measurement",
    "medication_unit_of_measurement",
    "medication_quantity",
    "medication_price",
    "dosage_type",
    "medication_dosage",
    "client_type",
    "quantity_unit_type",
    "supplier",
    "client",
    "medication_quantity_unit",
    "buyer",
    "medication_order",
    "prescription_dosage",
    "recipient_type",
    "recommended_dosage",
    "warehouse",
    "store",
    "product_category",
    "product_type",
    "warehouse_product",
    "warehouse_stock",
    "product_stock_unit",
    "order_batch",
    "department_stock_order",
    "product_price",
    "department_product_stock_unit",
    "lab_test_order_cart",
    "lab_test_order_details",
    "lab_test_results_category",
    "lab_test_results_parameters",
    "lab_test_results_type",
    "lab_results_method",
    "lab_test_results",
    "test_consumable",
    "lab_test_results_upload",
    "lab_test_price",
    "lab_test_bill",
    "mode_of_payment",
    "company",
    "payment",
    "payment_detail",
    "lab_test_ordered_sample",
    "lab_test_ordered_site",
    "department",
    "religion",
    "person_title",
    "occupation",
    "marital_status",
    "status",
    "allergies",
    "relative_type",
    "relative",
    "consulting_room",
    "sponsor_type",
    "sponsor",
    "sponsor_patient",
    "clinic_type",
    "attendance_type",
    "select_unit",
    "diagnosis",
    "consultation",
    "consultation_diagnosis",
    "procedure",
    "diagnosed_procedure",
    "facility_category",
    "product",
    "progress_bar",
    "service_charge_sponsor",
    "patient_service_charge",
    "payment_individual",
    "payment_by_sponsor",
    "payment_detail_Individual",
    "payment_detail_by_sponsor",
    "procedure_charge",
    "procedure_charge_by_sponsor",
    "procedure_schedule",
    "product_price_sponsor",
    "lab_test_price_sponsor",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:9000",
    "https://ehealth-hepeps-original.netlify.app",
]

ROOT_URLCONF = "hims_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hims_api.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# Use dev db when DEBUG is true else ...
DATABASES = (
    {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    if DEBUG == False
    else {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(hours=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
DBBACKUP_STORAGE = "django.core.files.storage.FileSystemStorage"
DBBACKUP_STORAGE_OPTIONS = {"location": os.path.join(BASE_DIR, "backup")}
CRONJOBS = [("*/1 * * * *", "hims_api.cron.my_backup")]

# Heroku cloud postgres db config
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

else:
    # Mail config
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = str(os.getenv("EMAIL_HOST"))
    EMAIL_USE_TLS = True
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_HOST_USER = str(os.getenv("EMAIL_HOST_USER"))
    EMAIL_HOST_PASSWORD = str(os.getenv("EMAIL_HOST_PASSWORD"))

# if not DEBUG:
#     # DB Config
#     django_on_heroku.settings(locals())
#     db_from_env = dj_database_url.config(conn_max_age=600)
#     DATABASES["default"].update(db_from_env)
