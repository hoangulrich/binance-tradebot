from variables import globalVar
from module.getPrice import *
from module.newMarketOrder import newMarketOrder
from utils.printColor import *

 # FIX ORDER IMMEDIATELY TRIGGER ERROR
def fixOrder(errorType):
    if errorType == "trigger" and globalVar.x <= globalVar.Xmax:
        
        # X EVEN
        if globalVar.x % 2 == 0 and globalVar.x != 0:
            price = getPrice(globalVar.symbol)
            if price > globalVar.initialCeiling:
                
                print(f"Price({price}) > Ceiling({globalVar.initialCeiling}) => CREATE new market order short sell")
                newMarketOrder(globalVar.symbol, "SHORT", "SELL", "MARKET", globalVar.quantity)
            else:
                from components.loopOrder import loopShort
                print(f"Price({price}) < Ceiling({globalVar.initialCeiling}) => loop short")
                loopShort(globalVar.quantity)
                
        # X ODD
        elif globalVar.x % 2 != 0 and globalVar.x != 0:
            price = getPrice(globalVar.symbol)
            if price < globalVar.initialFloor:
                print(f"Price({price}) < Floor({globalVar.initialFloor}) => CRAETE new market order long buy")
                newMarketOrder(globalVar.symbol, "LONG", "BUY", "MARKET", globalVar.quantity)
            else:
                from components.loopOrder import loopLong
                print(f"Price({price}) > Floor({globalVar.initialFloor}) => loop long")
                loopLong(globalVar.quantity)
          
def fixExpired(positionSide):
    from components.loopOrder import loopShort, loopLong
    if positionSide == "LONG":
        prCyan("FIX => loop long")
        loopLong(globalVar.quantity)
    elif positionSide == "SHORT":
        prCyan("FIX => loop short")
        loopShort(globalVar.quantity)
    
        
        