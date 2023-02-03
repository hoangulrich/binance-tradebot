from binanceAPI.user import um_futures_client
from binance.lib.utils import config_logging
from binance.error import ClientError
import logging
from binanceAPI.teleBot import send_error

#config_logging(logging, logging.DEBUG)

# CANCEL ORDER OF SYMBOL
def cancelOrder(symbol):
    try:
        response = um_futures_client.cancel_open_orders(symbol=symbol, recvWindow=2000)
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
