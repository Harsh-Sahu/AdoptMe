from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name=""),
    path("findapet", views.findapet, name="findapet"),
    path("donate/", views.donate, name="donate"),
    path("adoptioninfo", views.adoptioninfo, name="adoptioninfo")
]
