from binanceAPI.user import um_futures_client
import logging

def getPrice(symbol):
    response = um_futures_client.ticker_price(symbol)
    return float(response["price"])