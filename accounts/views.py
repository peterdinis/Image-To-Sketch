from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = Profile.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('profilepage')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('homepage')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('loginpage')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'accounts/register.html', {'form': form})

def profilePage(request, pk):
    user = Profile.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)