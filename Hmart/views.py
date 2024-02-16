from django.http import HttpResponse
from django.shortcuts import render


def Main(request):
    return render(request,'index.html')

def LoginPage(request):
    return render(request,'login.html')

def CartPage(request):
    return render(request,'cart.html')


def ContactPage(request):
    return render(request,'contact.html')

def AboutPage(request):
    return render(request,'about.html')

def AccountPage(request):
    return render(request,'my-account.html')




