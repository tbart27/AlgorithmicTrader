import requests
import json
import os
from time import *

def getToken():
    getToken_url = "https://bravenewcoin.p.rapidapi.com/oauth/token"
    # reference code from link for payload and headers code snippet
    # https://rapidapi.com/BraveNewCoin/api/bravenewcoin?endpoint=apiendpoint_836afc67-19d2-45ae-bb56-c576cec9f602
    payload = """"""
    headers = {}
    response = requests.request("POST", getToken_url, data=payload, headers=headers)

    oauth_json = json.loads(response.text)
    authToken = oauth_json['access_token']
    return authToken


def assetTicker(token):
    assetTicker_url = "https://bravenewcoin.p.rapidapi.com/market-cap"
    # reference link below for x-rapidapi-key
    # https://rapidapi.com/BraveNewCoin/api/bravenewcoin?endpoint=apiendpoint_836afc67-19d2-45ae-bb56-c576cec9f602
    querystring = {"assetId":""}
    headers = {
        'authorization': "Bearer {}".format(token),
        'x-rapidapi-key': "",
        'x-rapidapi-host': "bravenewcoin.p.rapidapi.com"
        }

    response = requests.request("GET", assetTicker_url, headers=headers, params=querystring)
    ticker_json = json.loads(response.text)['content'][0]
    return ticker_json

token = getToken()
if not os.path.exists("data/history.csv"):
    with open("data/history.csv", "a") as fp:
        fp.write("date,value\n")
for _ in range(0,100):
    with open("data/history.csv", "a") as fp:
        ticker_json = assetTicker(token)
        timestamp = ticker_json['timestamp'].split(":")[0] + ":" + ticker_json['timestamp'].split(":")[1]
        update = timestamp + "," + str(ticker_json['price'])
        print(update)
        fp.write(update + "\n")
        sleep(300)