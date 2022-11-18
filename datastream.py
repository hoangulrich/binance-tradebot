import logging
import websocket
import json, requests
from binance.lib.utils import config_logging
from user import um_futures_client, key
from module import *

# config_logging(logging, logging.DEBUG)

# END POINT URL
BINANCE_FUTURES_END_POINT = "https://fapi.binance.com/fapi/v1/listenKey"
FUTURES_STREAM_END_POINT_1 = "wss://fstream.binance.com"
FUTURES_STREAM_END_POINT_2 = "wss://fstream-auth.binance.com"

# GET LISTEN KEY
def create_futures_listen_key(api_key):
    response = requests.post(url=BINANCE_FUTURES_END_POINT, headers={'X-MBX-APIKEY': api_key})
    return response.json()['listenKey']

listen_key = create_futures_listen_key(key)

futures_connection_url = f"{FUTURES_STREAM_END_POINT_1}/ws/{listen_key}"


