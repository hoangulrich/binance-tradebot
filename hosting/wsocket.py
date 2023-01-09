import websocket, json
from utils.printColor import *
from algorithm import *
from binanceAPI.datastream import futures_connection_url
from utils.teleBot import *

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

def on_close(ws, close_status_code, close_msg):
    print(f"Close: {close_status_code} {close_msg}")

def run_stream():
    ws = websocket.WebSocketApp(url=futures_connection_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.run_forever(ping_interval=300)