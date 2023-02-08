import variables.globalVar as globalVar
from module.takeProfit import takeProfit
from utils.printColor import *
from binanceAPI.teleBot import *
from module.cancelOrder import cancelOrder

# BREAK EVEN LONG LAST FILLED
def endLong():
    cancelOrder(globalVar.symbol)
    prCyan("CANCEL ALL ORDERS(endLong)")

    # TP_LONG = round(globalVar.initialCeiling*(1+globalVar.profit/globalVar.leverage),globalVar.decimalPrecision)
    # SL_SHORT = TP_LONG
    # takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    # takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)
    # SL_LONG = round(globalVar.initialCeiling-(globalVar.initialCeiling-globalVar.initialFloor)*30/100,globalVar.decimalPrecision)
    # takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)

    # TP_SHORT = globalVar.initialFloor-(round(offsetFee,globalVar.decimalPrecision))
    # takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
<<<<<<< Updated upstream
    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)

    SL_LONG = round(globalVar.initialCeiling-(globalVar.initialCeiling-globalVar.initialFloor)*30/100,globalVar.decimalPrecision)
    offsetFee = round(globalVar.initialFloor,2)*0/100 
    TP_SHORT = globalVar.initialFloor-(round(offsetFee,globalVar.decimalPrecision))
=======
>>>>>>> Stashed changes

    TP_LONG = round(globalVar.initialCeiling*105/100,globalVar.decimalPrecision)
    TP_SHORT = round(globalVar.initialFloor*95/100,globalVar.decimalPrecision)
    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)

# BREAK EVEN SHORT LAST FILLED    
def endShort():
    cancelOrder(globalVar.symbol)
    prCyan("CANCEL ALL ORDERS(endShort)")

<<<<<<< Updated upstream
    SL_LONG = round(globalVar.initialFloor*(1-globalVar.profit/globalVar.leverage),globalVar.decimalPrecision)
    TP_SHORT = SL_LONG

    takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)

    offsetFee = round(globalVar.initialCeiling,2)*0/100
    TP_LONG = globalVar.initialCeiling+(round(offsetFee,globalVar.decimalPrecision))
    SL_SHORT = round(globalVar.initialFloor+(globalVar.initialCeiling-globalVar.initialFloor)*30/100,globalVar.decimalPrecision)
=======
    # SL_LONG = round(globalVar.initialFloor*(1-globalVar.profit/globalVar.leverage),globalVar.decimalPrecision)
    # TP_SHORT = SL_LONG
    # takeProfit(globalVar.symbol, "LONG", "SELL", "STOP_MARKET", SL_LONG)
    # takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
    # offsetFee = round(globalVar.initialCeiling,2)*0/100
    # SL_SHORT = round(globalVar.initialFloor+(globalVar.initialCeiling-globalVar.initialFloor)*30/100,globalVar.decimalPrecision)
    # takeProfit(globalVar.symbol, "SHORT", "BUY", "STOP_MARKET", SL_SHORT)
>>>>>>> Stashed changes

    # takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    # TP_LONG = globalVar.initialCeiling+(round(offsetFee,globalVar.decimalPrecision))

    TP_LONG = round(globalVar.initialCeiling*105/100,globalVar.decimalPrecision)
    TP_SHORT = round(globalVar.initialFloor*95/100,globalVar.decimalPrecision)
    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)

def endFinalLong():
    cancelOrder(globalVar.symbol)
<<<<<<< Updated upstream
    prCyan("CANCEL ALL ORDERS(endFinalLong)")
=======
    send_error("Breakeven triggered.")
>>>>>>> Stashed changes

    # offsetFee = round(globalVar.initialFloor,2)*0.2/100
    # TP_SHORT = globalVar.initialFloor-(round(offsetFee,globalVar.decimalPrecision)) 
    # takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)

    TP_SHORT = round(globalVar.initialFloor*95/100,globalVar.decimalPrecision)
    takeProfit(globalVar.symbol, "SHORT", "BUY", "TAKE_PROFIT_MARKET", TP_SHORT)
    
def endFinalShort():
    cancelOrder(globalVar.symbol)
<<<<<<< Updated upstream
    prCyan("CANCEL ALL ORDERS(endFinalShort)")

    offsetFee = round(globalVar.initialCeiling,2)*0.2/100
    TP_LONG = globalVar.initialCeiling+(round(offsetFee,globalVar.decimalPrecision))

=======
    send_error("Breakeven triggered.")
    
    # offsetFee = round(globalVar.initialCeiling,2)*0.2/100
    # TP_LONG = globalVar.initialCeiling+(round(offsetFee,globalVar.decimalPrecision))
    # takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
    
    TP_LONG = round(globalVar.initialCeiling*105/100,globalVar.decimalPrecision)
>>>>>>> Stashed changes
    takeProfit(globalVar.symbol, "LONG", "SELL", "TAKE_PROFIT_MARKET", TP_LONG)
