from variables.input import *
from hosting.wsocket import *
# from hosting.webserver import keep_alive
import variables.globalVar

def main():
    #keep_alive()
    if globalVar.x == 0:
        ask_input()
    run_stream()
    
if __name__ == "__main__":
    main()