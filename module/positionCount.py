from binanceAPI.user import um_futures_client
from binance.lib.utils import config_logging
from binance.error import ClientError
import variables.globalVar as globalVar
import logging
from binanceAPI.teleBot import send_error

# CHECK IF POSITION
def positionCount():
    try:
        response = um_futures_client.get_position_risk(symbol = globalVar.symbol)
        return len(response)       
    except ClientError as error:
        send_error("Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            ))
        logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )

