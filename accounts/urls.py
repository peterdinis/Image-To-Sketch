from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="loginpage"),
    path("register/", views.registerPage, name="registerpage"),
    path("logout/", views.logoutUser, name="logoutUser")
]