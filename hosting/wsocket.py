import websocket, json, threading, time, re
from utils.printColor import *
from algorithm import *
from binanceAPI.datastream import *
from utils.teleBot import *
from module.newMarketOrder import *

def on_open(ws):
    prGreen(f"Open: futures order stream connected")
    startLoop()
    
def on_message(ws, message):
    #prYellow(f"\nMessage: {message}\n")
    event_dict = json.loads(message)
    if event_dict["e"] == "ORDER_TRADE_UPDATE":
        if(event_dict["o"]["X"] == "FILLED"):
            
            # ASSIGN VARIABLE FOR FILLED ORDER
            filledPrice = event_dict["o"]["L"]
            filledQuantity = event_dict["o"]["l"]
            filledPositionSide = event_dict["o"]["ps"]
            filledStatus = event_dict["o"]["X"]
            
            #test2.3
            # send_error(f"price: {filledPrice}, quantity: {filledQuantity}, side: {filledPositionSide}, status: {filledStatus}")
            
            #run algo
            algorithm(filledPrice, filledQuantity, filledPositionSide, filledStatus)
        else:
            print("ORDER UPDATE: " + event_dict["o"]["ps"] + " " + event_dict["o"]["X"])
            
def on_error(ws, error):
    print(f"Error: {error}")
    # ORDER WOULD IMMEDIATELY TRIGGER ERROR
    if re.search("-2021") == True:
        if globalVar.x % 2 == 0:
            newMarketOrder(globalVar.symbol, "SHORT" , "SELL" ,"MARKET", globalVar.quantity)
        else:
            newMarketOrder(globalVar.symbol, "LONG" , "BUY" ,"MARKET", globalVar.quantity)

def on_close(ws, close_status_code, close_msg):
    print(f"Close: {close_status_code} {close_msg}")

def run_stream():
    ws = websocket.WebSocketApp(url=futures_connection_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    # ws.run_forever(ping_interval=300)
    
    wsthread = threading.Thread(target=ws.run_forever, daemon=True)
    wsthread.start()
    
    while True:
        time.sleep(900)
        keepAlive()