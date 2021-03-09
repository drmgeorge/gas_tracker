from web3 import Web3, middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

INFURA_PROJECT_ID = '20ef081861e8416d9bbac529008b668f'
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))

w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

w3.middleware_onion.add(middleware.time_based_cache_middleware)
w3.middleware_onion.add(middleware.latest_block_based_cache_middleware)
w3.middleware_onion.add(middleware.simple_cache_middleware)

def print_gas_price():

    #Gas price in wei therefore needs to be converted to Gwei
    gas_price = (w3.eth.generateGasPrice()) / 10**9
    print(gas_price)
    
    #Repeat forever
    print_gas_price()

print_gas_price()