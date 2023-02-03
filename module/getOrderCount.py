import logging
from binance.lib.utils import config_logging
from binance.error import ClientError
from binanceAPI.user import um_futures_client
from variables import globalVar

def getOrderCount(symbol):
    try:
        response = um_futures_client.get_orders(symbol=symbol, recvWindow=2000)
        return len(response)
        # return response
        # logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )