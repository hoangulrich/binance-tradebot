import variables.globalVar as globalVar
from module.newOrder import newOrder
from module.takeProfit import takeProfit
from utils.printColor import *
from module.cancelOrder import cancelOrder
from module.newMarketOrder import *

# CREATE ORDERS WHEN LONG FILLED
def loopLong(quantity):
    TP_LONG = round(globalVar.initialCeiling*(1+globalVar.profit/globalVar.leverage),globalVar.decimalPrecision)
    SL_SHORT = TP_LONG
    
    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)
    newOrder(globalVar.symbol, "SHORT", "SELL", "STOP_MARKET", quantity, globalVar.initialFloor)

# CREATE ORDERS WHEN SHORT FILLED
def loopShort(quantity):
    SL_LONG = round(globalVar.initialFloor*(1-globalVar.profit/globalVar.leverage),globalVar.decimalPrecision)
    TP_SHORT = SL_LONG
    
    takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
    newOrder(globalVar.symbol, "LONG", "BUY", "STOP_MARKET", quantity, globalVar.initialCeiling)
