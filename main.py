import json
from eth_account import account
from eth_utils import address
from web3 import Web3
from hexbytes import HexBytes


infura_url = 'https://mainnet.infura.io/v3/{your api key}'

web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
for i in range(1,10):
    account = web3.eth.account.create()
    address = account.address
    #print(address)
    privateKey = account.privateKey
    key = privateKey.hex()
    #print(key)

    f = open('list.txt', 'a')
    f.write('Address: ' + address + '\n' + 'PrivateKey: ' +key +'\n \n')
    f.close()