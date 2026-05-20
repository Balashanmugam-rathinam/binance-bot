import streamlit as st

from bot.orders import place_order
from bot.validators import validate_order

st.set_page_config(
    page_title="Trading Bot",
    page_icon="📈"
)

st.title("📈 Binance Futures Testnet Trading Bot")

symbol = st.text_input(
    "Symbol",
    value="BTCUSDT"
)

side = st.selectbox(
    "Side",
    ["BUY", "SELL"]
)

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)

quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.001
)

price = None

if order_type == "LIMIT":

    price = st.number_input(
        "Price",
        min_value=1.0,
        value=100000.0
    )

if st.button("Place Order"):

    try:

        validate_order(
            side,
            order_type,
            quantity,
            price
        )

        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        st.success("Order placed successfully!")

        st.json({
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice")
        })

    except Exception as e:

        st.error(str(e))