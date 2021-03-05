from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['confirm_password']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('regiser')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name = last_name, email=email, username = username, password = password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
            
        return redirect("/")
                            

    else:
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'user does not exist')
            
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
   