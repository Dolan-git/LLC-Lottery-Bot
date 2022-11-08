import requests
import os

HANDLE_POLICY_ID = 'f0ff48bbb7bbe9d59a40f1ce90e9e9d0ff5002ec48f232b49ca0fb9a'
BASE_URL = 'https://cardano-mainnet.blockfrost.io/api/v0'
PROJECT_ID = os.getenv('PROJECT_ID')


# resolves an ada handle and returns the associated stake key
def resolveAdaHandle(handle):
    headers = {
        'project_id': PROJECT_ID
    }

    handleHex = handle.encode().hex()

    fullAssetName = HANDLE_POLICY_ID + handleHex
    url = BASE_URL + f'/assets/{fullAssetName}/addresses'

    res = requests.get(url=url, headers=headers).json()

    return fetchStakeAddress(res[0]['address'])

def fetchStakeAddress(addr):
    headers = {
        'project_id': PROJECT_ID
    }

    url = BASE_URL + f'/addresses/{addr}'

    res = requests.get(url=url, headers=headers).json()

    return res['stake_address']

def fetchBalance(stake_addr):
    headers = {
        'project_id': PROJECT_ID
    }

    url = BASE_URL + f'/accounts/{stake_addr}'

    res = requests.get(url=url, headers=headers).json()

    print(res)

    return int(res.get('controlled_amount', 0)) / 1000000
