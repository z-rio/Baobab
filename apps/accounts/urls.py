from django.urls import path
from .views import CustomLogoutView, CustomRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", CustomRegistrationView.as_view(), name="register-user"),
    path("logout/", CustomLogoutView.as_view(), name="logout-user"),
    path("login/", TokenObtainPairView.as_view(), name="login-user"),
    path("refresh/login/", TokenRefreshView.as_view(), name="refresh-token"),
]
