from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("address", views.addAddress, name="address"),
]