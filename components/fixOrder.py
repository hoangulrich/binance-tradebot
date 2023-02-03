from variables import globalVar
from module.getPrice import *
from module.newMarketOrder import newMarketOrder

 # FIX ORDER IMMEDIATELY TRIGGER ERROR
def fixOrder(errorType):
    
    if errorType == "trigger" and globalVar.x <= globalVar.Xmax:
        
        # X Chan
        if globalVar.x % 2 == 0 and globalVar.x != 0:
            if getPrice(globalVar.symbol) > globalVar.initialCeiling:
                
                print("tao new market order short sell")
                newMarketOrder(globalVar.symbol, "SHORT", "SELL", "MARKET", globalVar.quantity)
            else:
                from components.loopOrder import loopShort
                print("loop short")
                loopShort(globalVar.quantity)
                
        # X Le
        elif globalVar.x % 2 != 0 and globalVar.x != 0:
            if getPrice(globalVar.symbol) < globalVar.initialFloor:
                print("tao new market order long buy")
                newMarketOrder(globalVar.symbol, "LONG", "BUY", "MARKET", globalVar.quantity)
            else:
                from components.loopOrder import loopLong
                print("loop long")
                loopLong(globalVar.quantity)
          
def fixExpired(positionSide):
    from components.loopOrder import loopShort, loopLong
    if positionSide == "LONG":
        print("loop long")
        loopLong(globalVar.quantity)
    elif positionSide == "SHORT":
        print("loop short")
        loopShort(globalVar.quantity)
    
        
        