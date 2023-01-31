import sys
sys.path.append('/repo_mcmct')
# Currency Converter

# The currencies and the exchange rates are saved in lists.
currencies_list = []
currency_usd = [0.92, 1.3, 0.7]
currency_eur = [1.09, 1.45, 0.88]
currency_cad = [0.75, 0.69, 0.61]
currency_gbp = [1.24, 1.14, 1.65]
currencies_list.append(currency_usd)
currencies_list.append(currency_eur)
currencies_list.append(currency_cad)
currencies_list.append(currency_gbp)


# The necessary user inputs.
base_currency = input("What is your base currency?\nType USD for American Dollars, EUR for Euros, CAD for Canadian Dollars and GBP for British (Pound) Sterling.").upper()
amount = float(input("Enter the amount for the currency exchange: "))
conversion = input("Enter currency to convert to (USD, EUR, CAD, GBP ...): ").upper()


# The main function for the currency conversion.
def convert(amount, rate):
    return amount * rate


# The querie which currency is the base, the amount in the base currency and the total value of the exchange.
match base_currency:
        case "USD":
            if conversion == "EUR":
                print("The amount is equivalent to: ", str(convert(amount, currencies_list[0][0])) + " \u20ac.")
            elif conversion == "CAD":
                print("The amount is equivalent to: ", str(convert(amount, currencies_list[0][1])) + " canadian \u0024.")
            elif conversion == "GBP":
                 print("The amount is equivalent to: ", str(convert(amount, currencies_list[0][2])) + " \u00a3.")
            else:
                 print("Invalid currency")
        case "EUR":
            if conversion == "USD":
                 print("The amount is equivalent to: ", str(convert(amount, currencies_list[1][0])) + " \u0024.")
            elif conversion == "CAD":
                print("The amount is equivalent to: ", str(convert(amount, currencies_list[1][1])) + " canadian \u0024.")
            elif conversion == "GBP":
                print("The amount is equivalent to: ", str(convert(amount, currencies_list[1][2])) + " \u00a3.")
            else:
                print("Invalid currency")
        case "CAD":
            if conversion == "USD":
                 print("The amount is equivalent to: ", str(convert(amount, currencies_list[2][0])) + " \u0024.")
            elif conversion == "EUR":
                print("The amount is equivalent to: ", str(convert(amount, currencies_list[2][1])) + " \u20ac.")
            elif conversion == "GBP":
                 print("The amount is equivalent to: ", str(convert(amount, currencies_list[2][2])) + " \u00a3.")
            else:
                 print("Invalid currency")
        case "GBP":
             if conversion == "USD":
                 print("The amount is equivalent to: ", str(convert(amount, currencies_list[3][0])) + " \u0024.")
             elif conversion == "EUR":
                 print("The amount is equivalent to: ", str(convert(amount, currencies_list[3][1])) + " \u20ac.")
             elif conversion == "CAD":
                 print("The amount is equivalent to: ", str(convert(amount, currencies_list[3][2])) + " canadian \u0024.")
             else:
                 print("Invalid currency")