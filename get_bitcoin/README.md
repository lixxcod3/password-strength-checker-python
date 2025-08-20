# Bitcoin to USD Calculator (CoinCap v3 API)

This project is a simple command-line program that converts a given amount of **Bitcoin (BTC)** to its equivalent value in **US Dollars (USD)** using real-time data from the [CoinCap API](https://coincap.io/).

---

## Features
- Fetches the latest Bitcoin price in USD from the CoinCap API.
- Allows the user to input an amount of BTC via the command line.
- Converts the input amount into USD and displays the result with comma formatting and 4 decimal places.
- Handles common errors:
  - Missing command-line arguments  
  - Invalid number inputs  
  - API request issues  

---

## Requirements
- Python 3.x  
- `requests` library
- Sign in to [CoinCap Sign-in](https://pro.coincap.io/signin) to get authorization code

Install dependencies with:
```bash
pip install requests
```

## How to Run the Program
```bash
python get_bitcoin.py (amount of btc)
```
Example:
```bash
python get_bitcoin.py 1.5

```


