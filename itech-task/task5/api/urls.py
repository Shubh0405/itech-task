from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('v1/calulate',views.display_result,name="calculate"),
]
