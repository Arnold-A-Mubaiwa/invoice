from enum import unique
from pydoc import describe
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
    address = models.ForeignKey(Address, on_delete= models.DO_NOTHING)
    phone_number = models.CharField(max_length = 15)
    email = models.EmailField( max_length=254)

class To(models.Model):
    recepiant_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField(max_length=254)

class Employee(models.Model):
    employee_id = models.CharField( max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length = 250)

class invoice(models.Model):
    invoice_number = models.CharField(max_length=9)
    invoice_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    generated_by = models.CharField(max_length=250)
    employee_id = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)

class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=250)
    describion = models.CharField(max_length = 500)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)