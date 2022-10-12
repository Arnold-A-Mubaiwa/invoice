from django.contrib import admin
from .models import Product, Employee, Company, To, Address
# Register your models here.

admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(To)
admin.site.register(Address)