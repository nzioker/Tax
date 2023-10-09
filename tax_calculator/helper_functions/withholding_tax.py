WITHHOLDING_TAX_CATEGORIES = {
    "Artists_and_entertainers": [0, 0.2],
    "Management_fees": [0.05, 0.2],
    "Professional_fees": [0.05, 0.2],
    "Training_fees": [0.05, 0.2],
    "Gaming_and_gambling": [0.2, 0.2],
    "Royalties": [0.05, 0.2],
    "Dividends": [0.1, 0.15],
    "Equipment_leasing": [0, 0.05],
    "Bank_interest": [0.15, 0.15],
    "Housing_bond_interest": [0.1, 0.15],
    "Government_bearer_bonds": [0.15, 0.15],
    "Other_bearer_bonds": [0.25, 0.25],
    "Bearer_bonds_maturity_of_over_10yrs": [0.1, 0],
    "Rent_buildings": [0.1, 0.3],
    "Rent_others": [0, 0.15],
    "Pension": [0.1, 0.05],
    "Insurance_commisions_brokers": [0.05, 0.2],
    "Insurance_commissions_others": [0.1, 0.2],
    "Consultancy_and_agency": [0.05, 0.2],
    "Contractual": [0.03, 0.2],
    "Telecommunication_services": [0, 0.05],
    "Natural_resource_income": [0.05, 0.2],
    "Digital_content_monetization": [0.05, 0.2],
    "Sales_promotion": [0.05, 0.2],
    "Withholding_on_rental_income_tax": [0.075, 0],
    "Gains_from_financial_derivatives": [0, 0.15],
}


def submit_input(category, residence, amount):
    tax_due = amount * WITHHOLDING_TAX_CATEGORIES[category][residence]
    return tax_due
