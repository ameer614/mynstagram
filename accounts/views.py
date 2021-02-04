from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from .forms import Create_new_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method == "POST":
        form = Create_new_user(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "accounts/login.html", {"form": form})
    else:
        form = Create_new_user()
        return render(request, "accounts/login.html", {"form": form})

def login_view(request):
    if request.method=='POST':
        email = request.POST('email')
        password=request.POST('password')
        user=authenticate(email=email,password=password)

        if user:
            login(request,user)
            return redirect('posts/home.html')
        else:
            return render(request,'accounts/loginn.html', {'error':True}) 
    return render(request,'accounts/loginn.html')
