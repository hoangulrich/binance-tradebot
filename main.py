from algorithm import *
from module.getBalance import *
import globalVar

def main():
    globalVar.initialBalance = getBalance()
    ask_input()
    run_stream()
    

if __name__ == "__main__":
    main()