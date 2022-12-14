from email import message
from importlib.abc import Loader
from turtle import st
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Address, Company,CompanyModel, ToModel
from django.template import loader

# Create your views here.
def index(request):
    return render(request, "home/address.html")
# adding to database
def addAddress(request):
    # not secure
    street = request.POST['street']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    zip = request.POST['zip']

    if (len(zip)>5):
        message = "The length of your zip code is too long"
        context = {
            "message": message
        }
        return render(request, "home/address.html", context)
    
    template = loader.get_template("home/address.html")
    
    new_addr = Address(street=street, city=city, state=state, country=country, zip_code = zip)
    if(new_addr):
        template = loader.get_template("home/success.html")
        new_addr.save()
        message = "Successful"
        return HttpResponse(template.render({'message':message}, request))
    else:
        return HttpResponse(template.render())

# def all_actions(self, request, id):
#     addAddress()
#     index()

def addCompany(request):
    if request.method == 'POST':
        form = CompanyModel(request.POST)
        if form.is_valid():
            form.save()
            message = "Form successfully saved"
            context = {
                'message':message,
                'form':form,
            }
            return render(request, 'home/addCompany.html',context)
    else:
        form = CompanyModel
        return render(request, 'home/addCompany.html',{'form':form})

def  addTo(request):
    if request.method == 'POST':
        form = ToModel(request.POST)
        if form.is_valid():
            form.save()
            message = "Form successfully saved"
            context = {
                'message':message,
                'form':form,
            }
            return render(request,'home/addto.html',context)
    else:
        form = ToModel
        return render(request,'home/addto.html',{'form':form})
