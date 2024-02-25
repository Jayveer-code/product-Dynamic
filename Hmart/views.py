from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product,Blog


def Main(request):
    
    SerData = Product.objects.all()
    blog_data = Blog.objects.all()
    data = {
        'SerData': SerData,
        'blog_data': blog_data
    } 
    return render(request,'index.html',data)
    

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

def ForgotPage(request):
    return render(request,'forgot.html')



