import variables.globalVar as globalVar
import os
from module.cancelOrder import cancelOrder
from module.getBalance import getBalance
from utils.printColor import *
from datetime import datetime
                
def restart_stream():    
    cancelOrder(globalVar.symbol)
    prGreen("DONE...Clear all orders\n")
    
    pnl = round(getBalance() - globalVar.initialBalance,2)
    duration = getDuration()
    record(pnl,duration)
    
    prYellow("-----RESTART-----\n")
    os.system('python "main.py"')
    
def getDuration():
    globalVar.end = datetime.now()
    duration = globalVar.end - globalVar.start
    duration = str(duration)[:-7]
    return duration

def record(pnl, duration):
    f = open("pnl.txt", "a")
    f.write("\n" + pnl + " " + duration + " " + globalVar.start + " " + globalVar.end)
    f.close()
    