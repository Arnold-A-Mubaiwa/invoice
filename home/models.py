from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=5)
    zip_code = models.CharField(max_length=5)

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_slogan = models.CharField(max_length=250)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length = 15)
    email = models.EmailField( max_length=254)

