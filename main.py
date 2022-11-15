from algorithm import *
from module import *
import globalVar
    
    # initialCeiling = 0.749
    # initialFloor = 0.745
    # symbol = "LITUSDT"
    # quantity0 = 30

def main():
    ask_input()

    newOrder(globalVar.symbol, "LONG","BUY","STOP_MARKET", globalVar.quantity0, globalVar.initialCeiling)
    newOrder(globalVar.symbol, "SHORT","SELL","STOP_MARKET", globalVar.quantity0, globalVar.initialFloor)
    run_stream()
    

if __name__ == "__main__":
    main()