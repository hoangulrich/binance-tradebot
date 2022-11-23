import os
import websocket
import json
import variables.globalVar as globalVar
from components.loopOrder import *
from components.endOrder import *
from components.printOrder import printOrder
from components.restart import restart_stream
from datetime import datetime
from binance.lib.utils import config_logging
from binanceAPI.user import um_futures_client, key
from module.cancelOrder import cancelOrder
from module.getBalance import getBalance
from module.positionIsEmpty import positionIsEmpty
from module.newMarketOrder import newMarketOrder
from module.takeProfit import takeProfit
from module.newOrder import newOrder
from utils.printColor import *

# CREATE NEW MARKET ORDER INITIALLY
def startLoop():
    globalVar.initialBalance = getBalance()
    globalVar.start = datetime.now()
    newMarketOrder(globalVar.symbol, "LONG","BUY","MARKET", globalVar.quantity)

# MAIN ALGORITHM
def algorithm(filledPrice, filledQuantity, filledPositionSide, filledStatus):
    
    # RESTART PROGRAM AND RECORD RESULT WHEN THERE ARE NO POSITION LEFT
    if positionIsEmpty() == True:
        restart_stream()
    
    # ASSIGN INITIAL CEILING/FLOOR
    if globalVar.x == 1:
        globalVar.initialCeiling = round(float(filledPrice),globalVar.decimalPrecision)
        globalVar.initialFloor = round(globalVar.initialCeiling-globalVar.gap*globalVar.initialCeiling,globalVar.decimalPrecision)
    
    # CALCULATE MARGIN/NAV AND PRINT INFORMATION
    globalVar.margin = round(float(filledQuantity)/globalVar.leverage*float(globalVar.initialCeiling),globalVar.decimalPrecision)
    globalVar.cumulativeMargin += globalVar.margin
    printOrder(filledPositionSide,filledStatus)
    
    # ???
    cancelOrder(globalVar.symbol)
    # prGreen("DONE...Clear all orders")
    
    # EVENT LOOP
    if globalVar.x < globalVar.Xmax:
        globalVar.x += 1
        quantity = globalVar.quantity*pow(2,globalVar.x)
        if filledPositionSide == "LONG":
            loopLong(quantity)
        else:
            loopShort(quantity)
        prGreen("DONE...Set up new open order")
    # X REACH XMAX    
    else:
        print("\nReaching maximum order at order no." + str(globalVar.x))
        if filledPositionSide == "LONG":
            endLong()
        else:
            endShort()
        prGreen("DONE...Breakeven stoploss strategy has been triggered.")