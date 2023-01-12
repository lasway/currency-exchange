import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
target_currency = os.getenv("target_currency")

baseCurrency = input('Enter base Currency for conversion:')
print('Target currency is set to:', target_currency)
Amount = input('Enter amount:')

URL = 'https://v6.exchangerate-api.com/v6/{}/pair/{}/{}/{}'.format(API_KEY, baseCurrency, target_currency, Amount)

r = requests.get(URL)

if r.status_code == 200:
    data = r.json()
    results = data['conversion_result']
    print('The Conversion is', results)

else:
    print('ERROR')
