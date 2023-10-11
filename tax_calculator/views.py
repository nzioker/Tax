from django.shortcuts import render
from django.http import HttpResponse
from tax_calculator.income_tax import Calculate_income_Tax
from tax_calculator.advance_tax import Advance_Tax
from tax_calculator.capital_gains_tax import Capital_Gains_tax
from tax_calculator.rental_income_tax import Rental_Income_Tax
from tax_calculator.withholding_tax import Withholding_tax


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Tax Calculator App")


def income_tax(request):
    employee_income_tax = Calculate_income_Tax()
    if request.method == "POST":
        NHIF = request.POST.get("nhif")
        NSSF = request.POST.get("nssf")
        housing_levy = request.POST.get("housing_levy")
        pension = request.POST.get("pension")

        net_pay = employee_income_tax.income_tax_calculator(1000000)
    return render(request, "tax_calculator/income_tax.html")


def advance_tax(request):
    a_tax = Advance_Tax()
    if request.method == "POST":
        advance_tax_category = request.POST.get("advance_tax")
        capacity = int(request.POST.get("advance_tax_capacity"))
        final_advance_tax = a_tax.calculate_advance_tax(advance_tax_category, capacity)
        # print(final_advance_tax)
        return render(
            request,
            "tax_calculator/advance_tax.html",
            {"final_advance_tax": final_advance_tax},
        )
    return render(request, "tax_calculator/advance_tax.html")


def capital_gains_tax(request):
    calculate_cgt = Capital_Gains_tax()
    if request.method == "POST":
        total_gains = int(request.POST.get("capital_gains_tax"))
        final_cgt = calculate_cgt.calculate_capital_gains_tax(total_gains)
        balance = total_gains - final_cgt
        return render(
            request,
            "tax_calculator/capital_gains_tax.html",
            {"final_cgt": final_cgt, "balance": balance},
        )
    return render(request, "tax_calculator/capital_gains_tax.html")


def rental_income_tax(request):
    rental_income = Rental_Income_Tax()
    if request.method == "POST":
        total_rental_income = int(request.POST.get("annual_rent"))
        final_rental_income_tax = rental_income.calculate_rental_income_tax(
            total_rental_income
        )
        return render(
            request,
            "tax_calculator/rental_income.html",
            {"final_rental_income_tax": final_rental_income_tax},
        )
    return render(request, "tax_calculator/rental_income.html")


def withholding_tax(request):
    calculate_withholding_tax = Withholding_tax()
    if request.method == "POST":
        withholding_tax_category = request.POST.get("withholding_tax_category")
        amount = int(request.POST.get("withholding_tax"))
        residency = calculate_withholding_tax.check_residency(
            request.POST.get("resident_type")
        )
        final_withholding_tax = calculate_withholding_tax.submit_input(
            withholding_tax_category, residency, amount
        )
        return render(
            request,
            "tax_calculator/withholding_tax.html",
            {"final_withholding_tax": final_withholding_tax},
        )
    return render(request, "tax_calculator/withholding_tax.html")
