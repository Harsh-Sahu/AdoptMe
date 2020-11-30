from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("contact/", views.contact, name="ContactUs"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),

]
