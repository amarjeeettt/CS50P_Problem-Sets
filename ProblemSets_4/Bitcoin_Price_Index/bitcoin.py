# Import necessary modules: sys for command-line arguments and requests for HTTP requests
import sys
import requests

try:
    # Check if the number of command-line arguments is 1 (no additional arguments provided)
    if len(sys.argv) == 1:
        sys.exit('Missing command-line argument')  # Exit with an error message

    # Check if the first command-line argument is alphabetic (not a number)
    elif sys.argv[1].isalpha():
        sys.exit('Command-line argument is not a number')  # Exit with an error message

    # Send an HTTP GET request to fetch the current Bitcoin price in USD
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    # Extract the Bitcoin price in USD from the JSON response
    btc_price = r.json()['bpi']['USD']['rate_float']

    # Calculate the amount in USD based on the provided Bitcoin quantity
    amount_quantity = float(btc_price) * float(sys.argv[1])

    # Print the calculated amount in USD with proper formatting (four decimal places and thousands separator)
    print(f"${amount_quantity:,.4f}")

# Handle exceptions, including requests.RequestException (for network errors)
except requests.RequestException:
    sys.exit()
