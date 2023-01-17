import variables.globalVar as globalVar
import os
from module.cancelOrder import cancelOrder
from module.getBalance import getBalance
from utils.printColor import *
from datetime import datetime
from binanceAPI.teleBot import *
# from hosting.wsocket import ws

def restart_stream():
  cancelOrder(globalVar.symbol)
  prGreen("DONE...Clear all orders\n")

  # CALCULATE PNL + DURATION
  pnl = round(getBalance() - globalVar.initialBalance, 4)
  duration = getDuration()
  record(pnl, duration)
  send_error("PNL: " + str(pnl) + "Gain: " + str(round(pnl/globalVar.cumulativeMargin*100,2)) +"%")
  send_error("-----RESTART-----")
  print("PNL: " + str(pnl) + "Gain: " + str(round(pnl/globalVar.cumulativeMargin*100,2)) + "%" + "\n-----RESTART-----\n")

  # LOCAL RESTART 
  os.system('python "main.py"')

  # SERVER RESTART
  # 1
  # @reboot /bin/python3 /home/ubuntu/binance-tradebot/main.py
  # 2 (chmod 755 launcher.sh)
  # @reboot sh /home/ubuntu/launcher
  # ws.close()
  # 3
  # os.execv(sys.executable,['python3'] + sys.argv)
  # 4 (chmod 755 main.py)
  # os.execv(sys.argv[0], sys.argv)


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
