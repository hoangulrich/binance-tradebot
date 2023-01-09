import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

TOKEN = config["TOKEN"]
chat_id = config["chat_id"]

def send_error(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message

    