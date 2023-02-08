import variables.globalVar as globalVar
from module.cancelOrder import cancelOrder
from module.getBalance import getBalance
from utils.printColor import *
from datetime import datetime
from binanceAPI.teleBot import *
from components.startLoop import initialOrder
from input import *

def restart_stream():
  # CLEAR LEFTOVER ORDERS
  cancelOrder(globalVar.symbol)
  prCyan("CANCEL ALL ORDERS(restart)")

  # CALCULATE PNL AND DURATION
  pnl = round(getBalance() - globalVar.initialBalance, 4)
  duration = getDuration()
  record(pnl, duration)

  # SEND INFO TELEGRAM
  send_error("PNL: " + "$" + str(pnl) + "\nGain: " + str(round(pnl/globalVar.cumulativeMargin*100,2)) +"%"
  + "\n*******RESTART*******")
  prCyan("RESTART")

  # RESTART
  ask_input()
  initialOrder()
  

def getDuration():
  globalVar.end = datetime.now()
  duration = globalVar.end - globalVar.start
  duration = str(duration)[:-7]
  return duration


def record(pnl, duration):
  f = open("pnl.txt", "a")
  f.write("\n" + str(globalVar.symbol) + " " + str(round(getBalance(), 2)) +
          " " + str(pnl) + " " + str(round(pnl/globalVar.cumulativeMargin*100,2)) + "%" + " " + str(globalVar.x-1) + " " + str(duration) +
          " " + str(globalVar.start) + " " + str(globalVar.end))
  f.close()