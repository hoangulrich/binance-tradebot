import logging
import json
from binance.lib.utils import config_logging
from binance.error import ClientError
from binanceAPI.user import um_futures_client
from utils.teleBot import send_error

config_logging(logging, logging.DEBUG)

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
        send_error("Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            ))
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )



