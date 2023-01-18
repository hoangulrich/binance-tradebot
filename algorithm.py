import variables.globalVar as globalVar
from components.loopOrder import *
from components.endOrder import *
from components.printOrder import printOrder
from components.restart import restart_stream
from module.cancelOrder import cancelOrder
from module.positionIsEmpty import positionIsEmpty
from module.positionCount import *
from utils.printColor import *
from binanceAPI.teleBot import *


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
    if positionCount == 2:
      if filledPositionSide == "LONG":
        endLong()
      else:
        endShort()
    if positionCount == 1:
      if filledPositionSide == "LONG":
        endFinalLong()
      else:
        endFinalShort()
    prGreen("DONE...Breakeven stoploss strategy has been triggered.")
    send_error("Reaching maximum order at order no." + str(globalVar.x)+ "\nBreakeven stoploss strategy has been triggered.")
