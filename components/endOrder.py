import variables.globalVar as globalVar
from module.takeProfit import takeProfit
from utils.printColor import *
from utils.teleBot import *
from module.cancelOrder import cancelOrder

# BREAK EVEN LONG LAST FILLED
def endLong():
    cancelOrder(globalVar.symbol)
  #new
    TP_LONG = round(globalVar.initialCeiling*(1+globalVar.profit/globalVar.leverage),globalVar.decimalPrecision)
    SL_SHORT = TP_LONG
    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)
    prGreen("DONE...Set up TP and SL Price")
    SL_LONG = round(globalVar.initialCeiling-(globalVar.initialCeiling-globalVar.initialFloor)*30/100,globalVar.decimalPrecision)
    offsetFee = round(globalVar.initialFloor,2)*0.2/100
    TP_SHORT = globalVar.initialFloor-(round(offsetFee,globalVar.decimalPrecision))
    
    takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
    # send_error("TP_LONG: " + str(TP_SHORT) + "\noffsetFee:" + str(offsetFee))

# BREAK EVEN SHORT LAST FILLED    
def endShort():
    cancelOrder(globalVar.symbol)
  #new
    SL_LONG = round(globalVar.initialFloor*(1-globalVar.profit/globalVar.leverage),globalVar.decimalPrecision)
    TP_SHORT = SL_LONG
    takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
    prGreen("DONE...Set up TP and SL Price")
    offsetFee = round(globalVar.initialCeiling,2)*0.2/100
    TP_LONG = globalVar.initialCeiling+(round(offsetFee,globalVar.decimalPrecision))
    
    SL_SHORT = round(globalVar.initialFloor+(globalVar.initialCeiling-globalVar.initialFloor)*30/100,globalVar.decimalPrecision)
    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)
    # send_error("TP_LONG: " + str(TP_LONG) + "\noffsetFee:" + str(offsetFee))
