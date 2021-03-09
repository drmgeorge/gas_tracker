# Ethereum Gas Tracker

## Install Web3
Setup a virtual environment by executing the following in the terminal
```
pip install virtualenv
virtualenv {NAME}
source {NAME}/bin/activate
```
Install Web3
```
pip install web3
```

## Integrate with Infura

* Create an Infura Account here: https://infura.io/
* Create a new project and copy the Project ID
* Paste the Project ID into index.js

```python
#index.js

INFURA_PROJECT_ID = 'project_id' #Change this
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))
```

## Running the script
 ```
python3 index.js
```
