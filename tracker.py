import requests
def get_prices(): 
    coins = ["BTC", "ETH", "BNB", "SOL", "XRP", "LUNA", "ADA", "DOGE", "AVAX", "DOT", "SHIB", "MATIC", "LTC", "TRX"] #Add any crypto coins you want :)
    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }
    return data