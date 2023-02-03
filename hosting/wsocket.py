import websocket, json, threading, time, re
from utils.printColor import *
from algorithm import *
from binanceAPI.datastream import *
from binanceAPI.teleBot import *
from module.newMarketOrder import *
from components.startLoop import initialOrder
from variables import globalVar
from components.fixOrder import *

def on_open(ws):
    exchange_info =  um_futures_client.exchange_info()
    for symbol in exchange_info["symbols"]:
        if symbol["symbol"] == globalVar.symbol:
            globalVar.decimalPrecision = symbol["pricePrecision"]
            globalVar.quantityPrecision = symbol["quantityPrecision"]
    initialOrder()
    
def on_message(ws, message):
    prYellow(f"\nMessage: {message}\n")
    event_dict = json.loads(message)
    #prYellow(json.dumps(event_dict, indent = 4))
    
    if event_dict["e"] == "ORDER_TRADE_UPDATE":
        if(event_dict["o"]["X"] == "FILLED"):
    
            # ASSIGN VARIABLE FOR FILLED ORDER
            filledPrice = event_dict["o"]["L"]
            filledQuantity = event_dict["o"]["l"]
            filledPositionSide = event_dict["o"]["ps"]
            filledStatus = event_dict["o"]["X"]
            
            # START ALGORITHM
            algorithm(filledPrice, filledQuantity, filledPositionSide, filledStatus)
            
        elif(event_dict["o"]["X"] == "EXPIRED"):
            print("fixEXPIRED")
            # -- TO DO --
            # fixOrder("expiredOrder")
        elif(event_dict["o"]["X"] == "PARTIALLY_FILLED"):
            print("fixPARTIAL")
        # else:
        #     print("ORDER UPDATE: " + event_dict["o"]["ps"] + " " + event_dict["o"]["X"])
            
def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Close: {close_status_code} {close_msg}")

def run_stream():
    ws = websocket.WebSocketApp(url=futures_connection_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    
    wsthread = threading.Thread(target = ws.run_forever, daemon = True)
    wsthread.start()
    
    while True:
        time.sleep(900)
        keepAlive()