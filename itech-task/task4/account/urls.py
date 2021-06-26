from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'account'

urlpatterns = [
    path('register/',views.RegisterView.as_view()),
    path('login/',views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
