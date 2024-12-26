from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('request/', views.GenerateOTPView.as_view(), name='request-otp'),
    path('verify/', views.VerifyOTPView.as_view(), name='verify-otp'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
