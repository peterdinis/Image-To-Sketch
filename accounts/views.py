from django.shortcuts import render

# Create your views here.
def loginpage(request):
    return render(request, 'accounts/login.html')

def registerpage(request):
    return render(request, 'accounts/register.html')

def profilepage(request):
    return render(request, 'accounts/profile.html')