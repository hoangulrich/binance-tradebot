from binance.um_futures import UMFutures
from dotenv import dotenv_values

config = dotenv_values(".env")

key = config["API_KEY"]
secret = config["API_SECRET"]

um_futures_client = UMFutures(key=key, secret=secret)