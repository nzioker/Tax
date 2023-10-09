from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("income_tax/", views.income_tax, name="income_tax"),
    path("advance_tax/", views.calculate_advance_tax, name="advance_tax"),
]
