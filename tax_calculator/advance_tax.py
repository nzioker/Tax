class Advance_Tax:
    def __init__(self):
        self.TAX_CATEGORIES = {
            "Vans_pickups_trailers_lorries_trucks": 1500,
            "Saloon_stationwagon_minibus_bus_coach": 60,
        }

    def calculate_advance_tax(self, category, capacity):
        advance_tax_payable = self.TAX_CATEGORIES[category] * capacity * 12
        if advance_tax_payable < 2400:
            return 2400
        return advance_tax_payable
