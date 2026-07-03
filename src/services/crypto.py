import requests

def get_crypto():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true"
    data = requests.get(url).json()

    return {
        "BTC": data["bitcoin"]["usd_24h_change"],
        "ETH": data["ethereum"]["usd_24h_change"]
    }
