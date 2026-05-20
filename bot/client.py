from binance.client import Client
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()


class BinanceFuturesClient:

    def __init__(self):

        api_key = os.getenv("BINANCE_API_KEY")

        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key:
            api_key = st.secrets.get(
                "BINANCE_API_KEY"
            )

        if not api_secret:
            api_secret = st.secrets.get(
                "BINANCE_API_SECRET"
            )

        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com/fapi"
        )

    def get_client(self):
        return self.client