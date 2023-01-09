import variables.globalVar as globalVar
from utils.printColor import *

def printOrder(filledPositionSide, filledStatus):
    prYellow("\n******Order no. " + str(globalVar.x) + "******")
    print("\nOrder no. " + str(globalVar.x) + " is " + filledStatus + " " + filledPositionSide)
    print("Order margin is " + str(globalVar.margin) + " USDT")
    print("Total NAV is " + str(round(globalVar.cumulativeMargin,2)) + " USDT")
    # print("Starting loop at",str(globalVar.start))
    # print("Current Ceiling Price is: " + str(globalVar.initialCeiling) + "\nCurrent Floor Price is: " + str(globalVar.initialFloor))
    prYellow("***Only have " + str(globalVar.Xmax-globalVar.x) + "/" + str(globalVar.Xmax) + " orders left.***")