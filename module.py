import logging
from binance.lib.utils import config_logging
from binance.error import ClientError
from user import um_futures_client

config_logging(logging, logging.DEBUG)

# NEW ORDER
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
        logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
# newOrder("LITUSDT", "SHORT", "SELL", "STOP_MARKET", 30, 0.732)

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
        logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )

#takeProfit("LITUSDT", "LONG", "SELL", "TAKE_PROFIT_MARKET", 0.728)

def cancelOrder(symbol):
    try:
        response = um_futures_client.cancel_open_orders(symbol=symbol, recvWindow=2000)
        logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )