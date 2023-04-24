from django.urls import path
from . import views


urlpatterns = [
    path("", views.default, name="defalut"),
    path("taxrate", views.rate, name="rate"),
    path("<str:price>", views.total_price, name="total_price")
]