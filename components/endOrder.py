import variables.globalVar as globalVar
from module.takeProfit import takeProfit
from utils.printColor import *

# BREAK EVEN LONG LAST FILLED
def endLong():
    #new
    TP_LONG = round(globalVar.initialCeiling*(1+globalVar.profit/globalVar.leverage),globalVar.decimalPrecision)
    SL_SHORT = TP_LONG
    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)
    prGreen("DONE...Set up TP and SL Price")
    SL_LONG = round(globalVar.initialCeiling-(globalVar.initialCeiling-globalVar.initialFloor)*90/100,globalVar.decimalPrecision)
    TP_SHORT = globalVar.initialFloor-(round(globalVar.initialFloor*0.15/100,globalVar.decimalPrecision))
    takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)

# BREAK EVEN SHORT LAST FILLED    
def endShort():
    #new
    SL_LONG = round(globalVar.initialFloor*(1-globalVar.profit/globalVar.leverage),globalVar.decimalPrecision)
    TP_SHORT = SL_LONG
    takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
    prGreen("DONE...Set up TP and SL Price")
    TP_LONG = globalVar.initialCeiling+(round(globalVar.initialCeiling*0.15/100,globalVar.decimalPrecision))
    SL_SHORT = round(globalVar.initialFloor+(globalVar.initialCeiling-globalVar.initialFloor)*90/100,globalVar.decimalPrecision)
    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)