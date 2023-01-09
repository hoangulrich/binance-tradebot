import variables.globalVar as globalVar
from components.loopOrder import *
from components.endOrder import *
from components.printOrder import printOrder
from components.restart import restart_stream
from datetime import datetime
from module.cancelOrder import cancelOrder
from module.getBalance import getBalance
from module.positionIsEmpty import positionIsEmpty
from module.newMarketOrder import newMarketOrder
from utils.printColor import *
from utils.teleBot import *


# CREATE NEW MARKET ORDER INITIALLY
def startLoop():
  globalVar.initialBalance = getBalance()
  globalVar.start = datetime.now()
  # newMarketOrder(globalVar.symbol, "LONG", "BUY", "MARKET", globalVar.quantity)
  newMarketOrder(globalVar.symbol, "SHORT", "SELL", "MARKET",
                 globalVar.quantity)


# MAIN ALGORITHM
def algorithm(filledPrice, filledQuantity, filledPositionSide, filledStatus):

  # RESTART PROGRAM AND RECORD RESULT WHEN THERE ARE NO POSITION LEFT
  if positionIsEmpty() == True:
    restart_stream()

  # ASSIGN INITIAL CEILING/FLOOR
  if globalVar.x == 0:
    # LONG 1ST
    # globalVar.initialCeiling = round(float(filledPrice),globalVar.decimalPrecision)
    # globalVar.initialFloor = round(globalVar.initialCeiling - globalVar.gap * globalVar.initialCeiling,globalVar.decimalPrecision)
    
    # SHORT 1ST
    globalVar.initialFloor = round(float(filledPrice),globalVar.decimalPrecision)
    globalVar.initialCeiling = round(globalVar.initialFloor + globalVar.gap * globalVar.initialFloor,globalVar.decimalPrecision)

  # CALCULATE MARGIN/NAV AND PRINT INFORMATION
  globalVar.margin = round(
    float(filledQuantity) / globalVar.leverage *
    float(globalVar.initialCeiling), globalVar.decimalPrecision)
  globalVar.cumulativeMargin += globalVar.margin
  printOrder(filledPositionSide, filledStatus)



  # Clear orders to prevent bug before loop phase
  cancelOrder(globalVar.symbol)
  prGreen("DONE...Clear all orders")

  # EVENT LOOP
  if globalVar.x < globalVar.Xmax:
      #debug
    send_error(
    str(globalVar.symbol) + " " + "x: " + str(globalVar.x) + " " + "price: " +
    str(filledPrice) + " " + "margin: " + str(globalVar.margin) + " USDT " +
    "side: " + str(filledPositionSide) + " status: " + str(filledStatus))
    globalVar.x += 1
    quantity = globalVar.quantity * pow(2, globalVar.x)
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
    send_error("Reaching maximum order at order no." + str(globalVar.x)+ "\nBreakeven stoploss strategy has been triggered.")
