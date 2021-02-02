from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect

def log_in(request):
    return render(request, "accounts/login.html")