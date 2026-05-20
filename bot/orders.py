from binance.exceptions import BinanceAPIException

from bot.client import BinanceFuturesClient
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):

    try:

        # Create client INSIDE function
        client = BinanceFuturesClient().get_client()

        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":

            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Order Request: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"Order Response: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"Binance API Error: {e}")

        raise Exception(
            f"Binance API Error: {e.message}"
        )

    except Exception as e:

        logger.error(f"Unexpected Error: {str(e)}")

        raise Exception(str(e))