from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'login.html')

def registration_page(request):
    return render(request, 'registration.html')