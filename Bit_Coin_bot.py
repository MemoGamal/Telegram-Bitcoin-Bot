import requests
import time
Time_interval=10*60
Telegram_Bot_ID="ID_number"
Telegram_Bot_API="API_NUMBER"
Url_Api_key='API_KEY'
def Get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
     'start':'1',
     'limit':'2',
    }
    headers = {
     'Accepts': 'application/json',
     'X-CMC_PRO_API_KEY': Url_Api_key,
     }
    response=requests.get(url, headers=headers,params=parameters).json()
    btc_price=response["data"][0]["quote"]["USD"]["price"]
    eth_pric=response["data"][1]["quote"]["USD"]["price"]
    Telegram_msg=f"Btc price is: {btc_price} and eth is : {eth_pric}"
    return Telegram_msg

def send_prc_to_telegram(Telegram_Bot_API,Telegram_Bot_ID,msg):
    url=f"https://api.telegram.org/bot{Telegram_Bot_API}/sendMessage?chat_id={Telegram_Bot_ID}&text={msg}"
    requests.get(url)

def main():
   while True:
        Get_price()
        msg=Get_price()
        send_prc_to_telegram(Telegram_Bot_API,Telegram_Bot_ID,msg)
        time.sleep(Time_interval)

main()
