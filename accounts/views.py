from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid

# Create your views here.
def home(request):
    return render(request, "home.html")

def login_attempt(request):
    return render(request, "login.html")
    
def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')
                
            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')

            user_obj = User.objects.create(username = username, email = email)
            user_obj.set_password(password)

            profile_obj = Profile.objects.create(user = user_obj , token = str(uuid.uuid4))
            profile_obj.save()

            return redirect('/token')
        
        except Exception as e:
            print(e)
    return render(request, "register.html")

    
def sucess(request):
    return render(request, "sucess.html")

def token_send(request):
    return render(request, "token_send.html")