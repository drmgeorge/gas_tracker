import requests 
import time
from enum import Enum

ETHERSCAN_API_KEY = 'enter_api_key_here'
URL = f'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={ETHERSCAN_API_KEY}'


class GasPrice(Enum):
    SAFE = "SafeGasPrice"
    PROPOSE = "ProposeGasPrice"
    FAST = "FastGasPrice"

def print_gas_price(GasPrice):

    r = requests.get(url = URL) 
    data = r.json() 
    print(data)
    print(data['result'][GasPrice.value])

    while True:
        r = requests.get(url = URL) 
        data = r.json() 
        print(data['result'][GasPrice.value])

        time.sleep(1)

    if data['status'] != '1':
        print(f'Error: {data}')
        return

print_gas_price(GasPrice.SAFE)
