from importlib.abc import Loader
from turtle import st
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Address
from django.template import loader

# Create your views here.
def index(request):
    return render(request, "home/address.html")

def addAddress(request):
    street = request.POST['street']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    zip = request.POST['zip']
    template = loader.get_template("home/address.html")
    new_addr = Address(street=street, city=city, state=state, country=country, zip_code = zip)
    if(new_addr):
        new_addr.save()
        return HttpResponse("Saved successfully")
    else:
        return render(request, "home/address.html")