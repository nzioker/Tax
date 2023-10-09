class Calculate_income_Tax:
    def __init__(self):
        self.TAX_BRACKETS = [
            (24000, 0.1),
            (8333, 0.15),
            (467667, 0.3),
            (300000, 0.325),
            (800000, 0.35),
        ]
        self.MONTHLY_PERSONAL_RELIEF = 2400
        self.DEDUCTIBLES = {
            "NHIF": 500,
            "NSSF": 250,
            "HOUSING_LEVY": 0.015,
            "PENSION": 0.05,
        }

    # This function calculates your taxable_income which is gross pay less your mandatory deductibles(NHIF, NSSF, PENSION AND HOUSING LEVY)
    def taxable_income(self, income):
        total_taxable_income = income - (
            self.DEDUCTIBLES["NHIF"]
            + self.DEDUCTIBLES["NSSF"]
            + (self.DEDUCTIBLES["HOUSING_LEVY"] * income)
            + (self.DEDUCTIBLES["PENSION"] * income)
        )
        return total_taxable_income

    # Ths function calculates your
    def income_tax_calculator(self, income):
        net_pay = income - self.income_tax(income, self.taxable_income(income))
        return net_pay

    def income_tax(self, income, taxable_inc):
        total_taxes = 0
        for amount, tax in self.TAX_BRACKETS:
            taxed_amount = min(taxable_inc, amount)
            total_taxes += taxed_amount * tax
            income -= taxed_amount
            if income <= 0:
                break
        total_taxes -= self.MONTHLY_PERSONAL_RELIEF
        return total_taxes


income_one = Calculate_income_Tax()
