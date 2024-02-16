from django.http import HttpResponse
from django.shortcuts import render,redirect
from service.models import Product

def index(request):
    SerData=Product.objects.all()
    #for a in SerData:
    #print(a.name,a.description,a.price,a.image)

    data={
         'SerData':SerData
     }   
    return render(request,"index.html",data)

