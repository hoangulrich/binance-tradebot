import variables.globalVar as globalVar
from components.loopOrder import *
from components.endOrder import *
from components.printOrder import printOrder
from components.restart import restart_stream
from module.cancelOrder import cancelOrder
from module.positionIsEmpty import positionIsEmpty
from utils.printColor import *
from binanceAPI.teleBot import *

def algorithm(filledPrice, filledQuantity, filledPositionSide, filledStatus):

  # RESTART PROGRAM WHEN THERE ARE NO POSITION LEFT
  if positionIsEmpty() == True:
    restart_stream()

  # MAIN ALGORITHM
  else:
    # ASSIGN INITIAL CEILING/FLOOR
    if globalVar.x == 0:
      # LONG 1ST
      # globalVar.initialCeiling = round(float(filledPrice),globalVar.decimalPrecision)
      # globalVar.initialFloor = round(globalVar.initialCeiling - globalVar.gap * globalVar.initialCeiling,globalVar.decimalPrecision)
      
      # SHORT 1ST
      globalVar.initialFloor = round(float(filledPrice),globalVar.decimalPrecision)
      globalVar.initialCeiling = round(globalVar.initialFloor + globalVar.gap * globalVar.initialFloor,globalVar.decimalPrecision)

    # CALCULATE MARGIN/NAV
    globalVar.margin = round(float(filledQuantity) / globalVar.leverage * float(globalVar.initialCeiling), globalVar.decimalPrecision)
    globalVar.cumulativeMargin += globalVar.margin
    
    # SEND INFO TELEGRAM
    # -- TO DO --
    print("Phase " + str(globalVar.x))
    send_error("Phase " + str(globalVar.x))

    # CLEAR ORDERS
    cancelOrder(globalVar.symbol)
    
    # EVENT LOOP
    if globalVar.x < globalVar.Xmax:
      
      globalVar.x += 1
      # globalVar.quantity = globalVar.quantity * pow(2, globalVar.x)
      globalVar.quantity = globalVar.quantity * 2

      if filledPositionSide == "LONG":
        loopLong(globalVar.quantity)
      else:
        loopShort(globalVar.quantity)

    # LAST ORDER/BREAK EVEN
    else:
      globalVar.x += 1
      if globalVar.x == globalVar.Xmax + 1:
        if filledPositionSide == "LONG":
          endLong()
        else:
          endShort()
      if globalVar.x == globalVar.Xmax + 2:
        if filledPositionSide == "LONG":
          endFinalLong()
        else:
          endFinalShort()
    