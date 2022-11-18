import logging
import json
from binance.lib.utils import config_logging
from binance.error import ClientError
from user import um_futures_client

#config_logging(logging, logging.DEBUG)

# NEW ORDER (STOP MARKET)
def newOrder(symbol,positionSide,side,type,quantity,stopPrice): 
    try:
        response = um_futures_client.new_order(
            symbol = symbol,
            positionSide = positionSide,
            side = side,
            type = type,
            quantity = quantity,
            timeInForce = "GTC",
            stopPrice = stopPrice,
        )
        #logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )

# NEW ORDER (MARKET)
def newOrderMarket(symbol,positionSide,side,type,quantity): 
    try:
        response = um_futures_client.new_order(
            symbol = symbol,
            positionSide = positionSide,
            side = side,
            type = type,
            quantity = quantity,
        )
        #logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )

# TAKE PROFIT
def takeProfit(symbol,positionSide,side,type,stopPrice): 
    try:
        response = um_futures_client.new_order(
            symbol = symbol,
            positionSide = positionSide,
            side = side,
            type = type,
            stopPrice = stopPrice,
            timeInForce = "GTC",
            closePosition = "true",
        )
        #logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )

# CANCEL ORDER OF SYMBOL
def cancelOrder(symbol):
    try:
        response = um_futures_client.cancel_open_orders(symbol=symbol, recvWindow=2000)
        #logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

# GET FUTURE BALANCE USDT
def getBalance():
    try:
        response = um_futures_client.balance(recvWindow=6000)
        for i in response:
            if i["asset"] == "USDT":
                return float(i["availableBalance"])
    except ClientError as error:
        logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

# CHECK IF POSITION IS EMPTY
def positionEmpty():
    try:
        response = um_futures_client.get_position_risk(symbol = "ETHUSDT")
        trigger1 = float(response[0]["positionAmt"])
        trigger2 = float(response[1]["positionAmt"])
        # print(trigger1)
        # print(trigger2)
        
        if trigger1 == 0 and trigger2 == 0:
            # print("position = 0")
            return True
        else:
            # print("position > 0")
            return False         
    except ClientError as error:
        logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

