#! /usr/bin/python3
from input import *
from hosting.wsocket import *

def main():
    send_error("\n*******START*******")
    if globalVar.x == 0:
        ask_input()
    run_stream()
    
if __name__ == "__main__":
    main()