class Rental_Income_Tax:
    def __init__(self):
        self.MRI = 0.075

    def calculate_rental_income_tax(self, annual_rent):
        return annual_rent * self.MRI
