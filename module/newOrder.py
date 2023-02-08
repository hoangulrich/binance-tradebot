import logging
from binance.lib.utils import config_logging
from binance.error import ClientError
from binanceAPI.user import um_futures_client
from variables import globalVar
from binanceAPI.teleBot import send_error
from components.fixOrder import *

#config_logging(logging, logging.DEBUG)

# NEW ORDER (STOP MARKET)
def newOrder(symbol,positionSide,side,type,quantity,stopPrice): 
    try:
        response = um_futures_client.new_order(
            symbol = symbol,
            positionSide = positionSide,
            side = side,
            type = type,
            quantity = float(round(quantity,globalVar.quantityPrecision)),
            timeInForce = "GTC",
            stopPrice = stopPrice,
        )
        #logging.info(response)
    except ClientError as error:
        send_error("NewOrder error. Error code: {}, error message: {}".format(error.error_code, error.error_message))
        #logging.error("NewOrder error. Error code: {}, error message: {}".format(error.error_code, error.error_message))
        if error.error_code == -2021:
            fixOrder("trigger")
        



