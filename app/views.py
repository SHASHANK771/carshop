from django.shortcuts import render
from app.models import *

# Create your views here.
def carshop(request):
    if request.method=="POST":
        first=request.POST.get('first')
        last=request.POST.get('last')
        email=request.POST.get('email')
        address=request.POST.get('address')
        #number=request.POST.get('phone_number')
        #date=request.POST.get('date')
        #time=request.POST.get('time')
        c=Carshop.objects.get_or_create(first=first,last=last,email=email,address=address)[0]
        c.save()
    return render(request,'carshop.html')
h


def shash(request):
    if request.method=="POST":
        first=request.POST.get('first')
        last=request.POST.get('last')
        email=request.POST.get('email')
        address=request.POST.get('address')
        date=request.POST.get('date')
        number=request.POST.get('number')
        #date=request.POST.get(' date')
        #time=request.POST.get('time')
        s=Shash.objects.get_or_create(first=first,last=last,email=email,address=address,date=date,number=number)[0]
        s.save()
    return render(request,'shash.html')   
