from django.shortcuts import render
from django.http import HttpResponse
from user.models import User

# Create your views here.
def login_page(request):
    return render(request, 'login/index.html', {})

def submit_data(request):
    name = request.POST['name']
    pwd = request.POST['password']

    user = User.objects.filter(name=name)

    if user and user[0].password == pwd:
        return HttpResponse(f"Successfully login {user[0]}")
    else:
        return HttpResponse(f"Failed to login {name}")

def router(request):
    return render(request, 'router/index.html', {});

def logout(request):
    return render(request, 'logout/index.html', {});

def smiley(request):
    return render(request, 'smiley/index.html', {});

