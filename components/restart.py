import variables.globalVar as globalVar
import os
from module.cancelOrder import cancelOrder
from module.getBalance import getBalance
from utils.printColor import *
from datetime import datetime
from utils.teleBot import *


def restart_stream():
  cancelOrder(globalVar.symbol)
  # prGreen("DONE...Clear all orders\n")

  pnl = round(getBalance() - globalVar.initialBalance, 4)
  duration = getDuration()
  record(pnl, duration)
  send_error("PNL: " + "$" + str(pnl) + "\nGain: " + str(round(pnl/globalVar.cumulativeMargin*100,2)) +"%")
  send_error("----------RESTART----------")
  send_error(".")
  send_error(".")
  send_error(".")
  print("PNL: " + str(pnl) + "Gain: " + str(round(pnl/globalVar.cumulativeMargin*100,2)) + "%" + "\n-----RESTART-----\n")
  os.system('python "main.py"')


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
