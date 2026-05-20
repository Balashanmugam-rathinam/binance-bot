from binance.client import Client
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()


class BinanceFuturesClient:

    def __init__(self):

        api_key = (
            os.getenv("BINANCE_API_KEY")
            or st.secrets["BINANCE_API_KEY"]
        )

        api_secret = (
            os.getenv("BINANCE_API_SECRET")
            or st.secrets["BINANCE_API_SECRET"]
        )

        # IMPORTANT FIX
        self.client = Client(
            api_key=api_key,
            api_secret=api_secret,
            testnet=True
        )

        # Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client