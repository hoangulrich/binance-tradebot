import logging
import websocket
import json, requests
from binance.lib.utils import config_logging
from user import um_futures_client, key
from module import *
from datastream import futures_connection_url
import math
import globalVar

config_logging(logging, logging.DEBUG)

# INPUT
# initialCeiling = None
# initialFloor = None
# symbol = None
# quantity0 = None

# global symbol


def ask_input():
    globalVar.symbol = input('Enter Symbol: ')
    globalVar.initialCeiling = float(input('Enter Ceiling: '))
    globalVar.initialFloor = float(input('Enter Floor: '))
    globalVar.quantity0 = float(input('Enter Quantity: '))

# ALGORITHM ON DATASTREAM
def on_open(ws):
    print(f"Open: futures order stream connected")

def on_message(ws, message):
    TP_LONG = globalVar.initialCeiling*1.01
    SL_LONG = globalVar.initialFloor*0.99
    TP_SHORT = SL_LONG
    SL_SHORT = TP_LONG
    

    print(f"Message: {message}")
    event_dict = json.loads(message)
    if event_dict["e"] == "ORDER_TRADE_UPDATE":
        if(event_dict["o"]["X"] == "FILLED"):
            e = pow(2,globalVar.x)
            quantity1 = globalVar.quantity0*e
            if event_dict["o"]["ps"] == "LONG":
                cancelOrder(globalVar.symbol)
                newOrder(globalVar.symbol, "SHORT", "SELL", "STOP_MARKET", quantity1, globalVar.initialFloor)
                globalVar.x = globalVar.x + 1
                print(globalVar.x)
                print("new order of " + event_dict["o"]["X"] + "and side" + event_dict["o"]["ps"] + " at x = " + globalVar.x)
            else:
                cancelOrder(globalVar.symbol)
                newOrder(globalVar.symbol, "LONG", "BUY", "STOP_MARKET", quantity1, globalVar.initialCeiling)
                globalVar.x = globalVar.x + 1
                print(globalVar.x)
                print("new order of " + event_dict["o"]["X"] + "and side" + event_dict["o"]["ps"] + " at x = " + globalVar.x)
        else:
            print(event_dict["o"]["X"])
    # takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    # takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
    # takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
    # takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)

        # order_status = event_dict["X"]
        # if order_status == "NEW": 
        #     symbol = event_dict["s"]
        #     id = event_dict["i"]  # int
        #     price = event_dict["L"]  
        #     side = event_dict["S"]  
        #     qty = event_dict["l"] 
        #     fee = event_dict["n"]  
        #     print(f"{symbol}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Close: {close_status_code} {close_msg}")

def run_stream():
    ws = websocket.WebSocketApp(url=futures_connection_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.run_forever(ping_interval=300)

