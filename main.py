from variables.input import *
from hosting.wsocket import *
from hosting.webserver import keep_alive

def main():
    #keep_alive
    ask_input()
    run_stream()
    
if __name__ == "__main__":
    main()