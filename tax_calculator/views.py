from django.shortcuts import render
from django.http import HttpResponse
from tax_calculator.income_tax import Calculate_income_Tax
from tax_calculator.advance_tax import calculate_advance_tax


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Tax Calculator App")


def income_tax(request):
    employee_income_tax = Calculate_income_Tax()
    net_pay = employee_income_tax.income_tax_calculator(1000000)
    return HttpResponse(f"Your net pay is {net_pay}")


def advance_tax(request):
    employee_advance_tax = calculate_advance_tax(
        "Saloon_stationwagon_minibus_bus_coach", 3
    )
    print(employee_advance_tax)
    return HttpResponse(f"Your advance tax is {employee_advance_tax}")
