# Currency converter program
conversion_rates = {
    'USD': 1,
    'EUR': 0.85,
    'GBP': 0.75,
    'INR': 75.0
}

def convert_currency():
    print("\nAvailable currencies: USD, EUR, GBP, INR")
    from_currency = input("Enter the currency you want to convert from: ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()

    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        print("Invalid currency!")
        return

    amount = float(input(f"Enter the amount in {from_currency}: "))
    converted_amount = amount * (conversion_rates[to_currency] / conversion_rates[from_currency])
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

convert_currency()
