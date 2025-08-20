import sys
import json
import requests

""""
Bitcoin to US Dollar Calculator Coincap 
Note: to run the program type "python get_bitcoin.py (amount of btc)"
Example: python get_bitcoin.py 1.5

"""""

if len(sys.argv) == 2:
        try:
            x = float(sys.argv[1])  # this will fail if 'cat'
        except ValueError:
                print("Command-line argument is not a number")
                sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)


try:
    url = "https://rest.coincap.io/v3/assets/Bitcoin"
    headers = {
       "Authorization": "Bearer f4d76a29555ce4d72db62a17c836319c68a74d60a73309269222d51fbd8e486c"}
    response = requests.get(url, headers=headers)

    #print(json.dumps(response.json(), indent=2)) """"check data location""""

    r= response.json()
    price = float(r["data"]["priceUsd"])
    total_amount= price * x
    print(f"${total_amount:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)
