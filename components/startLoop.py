import variables.globalVar as globalVar
from module.newMarketOrder import *
from module.getBalance import *
from datetime import datetime
from module.newOrder import *
from utils.printColor import *

# CREATE NEW MARKET ORDER INITIALLY
def initialOrder():
  globalVar.initialBalance = getBalance()
  globalVar.start = datetime.now()
  
  prCyan("\nINITIAL ORDER")
  # newMarketOrder(globalVar.symbol, "LONG", "BUY", "MARKET", globalVar.quantity)
  newMarketOrder(globalVar.symbol, "SHORT", "SELL", "MARKET", globalVar.quantity)

