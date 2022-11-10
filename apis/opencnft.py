import requests

TICKET_POLICY_ID = 'd31438739943cc47adfa99947e086db735aa866b754152f0469b89d8'
BASE_URL = 'https://api.opencnft.io/1'

def fetchTicketsMinted():
    url = BASE_URL + f'/policy/{TICKET_POLICY_ID}'

    res = requests.get(url=url).json()

    return res.get("asset_minted", 0)
