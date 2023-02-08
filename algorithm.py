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
      send_error("\n*******START*******"+
                "\n - Current Ceiling Price is: " + str(round(globalVar.initialCeiling,4)) + 
                "\n - Current Floor Price is: " + str(round(globalVar.initialFloor,4)))

    # CALCULATE MARGIN/NAV
    globalVar.margin = round(float(filledQuantity) / globalVar.leverage * float(globalVar.initialCeiling), globalVar.decimalPrecision)
    globalVar.cumulativeMargin += globalVar.margin
    
    # SEND INFO TELEGRAM
    # -- TO DO --
    send_error("Order no. " + str(globalVar.x) + 
    "\n - Order is " + str(filledStatus) + " " + str(filledPositionSide) +
    "\n - Order margin is " + str(round(globalVar.margin,2)) + " USDT" +
    "\n - Total NAV is " + str(round(globalVar.cumulativeMargin,2)) + " USDT")
    print("\nPHASE " + str(globalVar.x))
    
    # EVENT LOOP
    if globalVar.x < globalVar.Xmax:
      
      globalVar.x += 1
      # globalVar.quantity = globalVar.quantity * pow(2, globalVar.x)
      globalVar.quantity = globalVar.quantity * 2

      if filledPositionSide == "LONG" and globalVar.expiredOrder == False:
        loopLong(globalVar.quantity)
      elif filledPositionSide == "SHORT" and globalVar.expiredOrder == False:
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
    