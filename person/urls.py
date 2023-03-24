from django.urls import path
from rest_framework import routers
from .views import (
    UserViewSet,
    PatientViewSet,
    StaffViewSet,
    LoginView,
    UserView,
    LogoutView,
    CombinedPatientView,
    LogoutAllView,
    ChangePasswordView,
    CombinedUserGroupView,
    ExistingUserAsPatientViewSet,
    PatientSearchView,
    PasswordResetRequestLinkView,
    PasswordResetView,
)

router = routers.DefaultRouter()
router.register("api/user", UserViewSet, "user")
router.register("api/patient", PatientViewSet, "patient")
router.register("api/staff", StaffViewSet, "staff")
router.register(
    "api/existing_user_as_patient",
    ExistingUserAsPatientViewSet,
    "existing_user_as_patient",
)
# router.register('api/patient_search', PatientSearchView, 'patient_search')

urlpatterns = [
    path("api/login", LoginView.as_view(), name="login"),
    # path('api/user', UserView.as_view(), name='user'),
    path("api/logout", LogoutView.as_view(), name="logout"),
    path("api/logout_all/", LogoutAllView.as_view(), name="logout_all"),
    path("api/patient_list", CombinedPatientView.as_view(), name="patient_list"),
    path(
        "api/change_password/<int:pk>/",
        ChangePasswordView.as_view(),
        name="change_password",
    ),
    path(
        "api/user_group_list", CombinedUserGroupView.as_view(), name="user_group_list"
    ),
    path("api/patient_search", PatientSearchView.as_view(), name="patient_search"),
    path(
        "api/password-reset/request",
        PasswordResetRequestLinkView.as_view(),
        name="password_request_link",
    ),
    path(
        "api/password-reset/verify/<str:token>",
        PasswordResetView.as_view(),
        name="password_reset",
    ),
]
urlpatterns += router.urls
