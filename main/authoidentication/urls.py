from . import views
from django.urls import path

urlpatterns = [
    path('login-register.html', views.register_user, name='login_register'),
    path('login-register.html', views.login_user, name='login_register'),
    path('login-register.html', views.log_out, name='login_register'),
]