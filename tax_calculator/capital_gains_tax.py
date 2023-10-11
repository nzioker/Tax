class Capital_Gains_tax:
    def __init__(self):
        self.CGT_RATE = 0.15

    def calculate_capital_gains_tax(self, gains_made):
        return gains_made * self.CGT_RATE
