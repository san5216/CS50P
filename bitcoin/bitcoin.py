import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Command-line argument is not a number")

o = response.json()
x = o.get("bpi").get("USD").get("rate_float")

amount = x * float(sys.argv[1])

print(f"${amount:,.4f}")



