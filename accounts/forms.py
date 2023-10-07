from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'name', 'username', 'email', 'bio']