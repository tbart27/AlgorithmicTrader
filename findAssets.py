import pandas as pd
import requests
import json


def findAssets():
    url = "https://bravenewcoin.p.rapidapi.com/asset"

    querystring = {"status": "ACTIVE"}

    headers = {
        "x-rapidapi-key": "",
        "x-rapidapi-host": "bravenewcoin.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    assets_json = json.loads(response.text)["content"]
    # print(assets_json)
    assetSymbol_list = [
        "BTC",
        "ETC",
        "LTC",
        "XRP",
        "USDT",
        "BCH",
        "DOT",
        "XMR",
        "EOS",
        "BUSD",
        "XTZ",
        "TRX",
        "ADA",
        "XLM",
        "DAI",
        "TUSD",
        "PAX",
        "USDC",
        "XEM",
        "DASH",
    ]
    for asset in assets_json:
        if asset["symbol"] in assetSymbol_list:
            print(
                "ID: {}; NAME: {}; SYMBOL: {}".format(
                    asset["id"], asset["name"], asset["symbol"]
                )
            )


findAssets()