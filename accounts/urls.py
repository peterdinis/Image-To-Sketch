from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="loginpage"),
    path("profile/", views.profilePage, name="profilepage"),
    path("register/", views.registerPage, name="registerpage"),
    path("logout/", views.logoutUser, name="logoutUser")
]