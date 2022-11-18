import os
import websocket
import json
from binance.lib.utils import config_logging
from user import um_futures_client, key
from module import *
from datastream import futures_connection_url
import globalVar

#config_logging(logging, logging.DEBUG)

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def ask_input():
    globalVar.leverage = 100
    globalVar.Xmax = 4
    globalVar.initialMargin = 0.25
    globalVar.symbol = "ETHUSDT"
    globalVar.gap = 0.05/100
    globalVar.takeprofit = 100/100
    globalVar.quantity0 = 0.005
    globalVar.x = 1

# ALGORITHM ON DATASTREAM
def on_open(ws):
    print(f"Open: futures order stream connected")
    newOrderMarket(globalVar.symbol, "LONG","BUY","MARKET", globalVar.quantity0)


def on_message(ws, message):
    #prYellow(f"\nMessage: {message}\n")
    event_dict = json.loads(message)
    if event_dict["e"] == "ORDER_TRADE_UPDATE":
        if(event_dict["o"]["X"] == "FILLED"):
            if positionEmpty() == True:
                pnl = getBalance() - globalVar.initialBalance
                prYellow(pnl)
                print("RESTART")
                os.system('python "main.py"')
                
            globalVar.initialCeiling = round(float(event_dict["o"]["L"]))
            globalVar.initialFloor = round(globalVar.initialCeiling-globalVar.gap*globalVar.initialCeiling,2)
            # globalVar.quantity0 = round(globalVar.initialMargin/globalVar.initialCeiling*globalVar.leverage,2)
            
            m = round(float(event_dict["o"]["q"])/globalVar.leverage*float(globalVar.initialCeiling),4)
            globalVar.cumm = globalVar.cumm + m
            #print("\n" + str(globalVar.cumm) + "\n")
            prYellow("\nOrder no. " + str(globalVar.x) + "********************************************")
            print("\nOrder no. " + str(globalVar.x) + " is " + str(event_dict["o"]["X"]) + " with position " + str(event_dict["o"]["ps"]))
            print("\nOrder margin is " + str(m) + " USDT " + "\nTotal NAV is " + str(globalVar.cumm) + " USDT")
            print("Current Ceiling Price is: " + str(globalVar.initialCeiling) + "\nCurrent Floor Price is: " + str(globalVar.initialFloor))
            print("***Only have " + str(globalVar.Xmax-globalVar.x) + "/" + str(globalVar.Xmax) + " orders left.***")
            e = pow(2,globalVar.x)
            quantity1 = globalVar.quantity0*e
            
            # LOOP
            if globalVar.x < globalVar.Xmax:
                if event_dict["o"]["ps"] == "LONG":
                    cancelOrder(globalVar.symbol)
                    prGreen("DONE...Clear all orders")
                    TP_LONG = round(globalVar.initialCeiling*(1+globalVar.takeprofit/globalVar.leverage),2)
                    SL_SHORT = TP_LONG
                    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
                    takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)
                    prGreen("DONE...Set up TP and SL Price\n")
                    newOrder(globalVar.symbol, "SHORT", "SELL", "STOP_MARKET", quantity1, globalVar.initialFloor)
                    globalVar.x += 1
                    
                else:
                    cancelOrder(globalVar.symbol)
                    prGreen("DONE...Clear all orders")
                    SL_LONG = round(globalVar.initialFloor*(1-globalVar.takeprofit/globalVar.leverage),2)
                    TP_SHORT = SL_LONG
                    takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
                    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
                    prGreen("DONE...Set up TP and SL Price\n")
                    newOrder(globalVar.symbol, "LONG", "BUY", "STOP_MARKET", quantity1, globalVar.initialCeiling)
                    globalVar.x += 1
                    
            # QUA XMAX -> BREAK EVEN  
            else:
                if event_dict["o"]["ps"] == "LONG":
                    cancelOrder(globalVar.symbol)
                    TP_LONG = round(globalVar.initialCeiling*1.01,2)
                    SL_SHORT = TP_LONG
                    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
                    takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)

                    SL_LONG = round(globalVar.initialCeiling-0.5,2)
                    TP_SHORT = globalVar.initialFloor
                    takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
                    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
                    print("\nNot enough Margin to run order no." + str(globalVar.x+1)
                     + "\nDONE...Breakeven stoploss strategy has been triggered. \nDONE...Bot has stopped working")
                         
                else:
                    cancelOrder(globalVar.symbol)
                    SL_LONG = round(globalVar.initialFloor*0.99,2)
                    TP_SHORT = SL_LONG
                    takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
                    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)

                    TP_LONG = globalVar.initialCeiling
                    SL_SHORT = round(globalVar.initialFloor+0.5,2)
                    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
                    takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)
                    print("\nNot enough Margin to run order no." + str(globalVar.x+1)
                     + "\nDONE...Breakeven stoploss strategy has been triggered. \nDONE...Bot has stopped working")
                                         
        else:
            print(event_dict["o"]["ps"] + " " + event_dict["o"]["X"])


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

