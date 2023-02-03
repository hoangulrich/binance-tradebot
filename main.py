#! /usr/bin/python3
from input import *
from hosting.wsocket import *

def main():
    if globalVar.x == 0:
        ask_input()
    run_stream()
    
if __name__ == "__main__":
    main()