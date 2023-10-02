from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginpage, name="loginpage"),
    path("profile/", views.profilepage, name="profilepage"),
    path("register/", views.registerpage, name="registerpage")
]