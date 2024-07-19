from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='index'),
    path('register-user', views.register_user, name='register_user'),
    path('log-in', views.login_user, name='login_user'),
    path('log-out', views.log_out, name='log_out'),
]