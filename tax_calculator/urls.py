from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("income_tax/", views.income_tax, name="income_tax"),
    path("advance_tax/", views.advance_tax, name="advance_tax"),
    path("capital_gains_tax/", views.capital_gains_tax, name="cgt"),
    path("rental_income_tax/", views.rental_income_tax, name="rental_income_tax"),
    path("withholding_tax/", views.withholding_tax, name="withholding_tax"),
]
