from binanceAPI.user import um_futures_client
from binance.lib.utils import config_logging
from binance.error import ClientError
import logging

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