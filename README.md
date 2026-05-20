# Binance Futures Testnet Trading Bot

A Python-based trading bot for Binance Futures Testnet (USDT-M) that supports MARKET and LIMIT orders through both CLI and Streamlit UI.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- Command Line Interface (CLI)
- Streamlit-based frontend UI
- Input validation
- Structured logging
- Exception handling
- Modular project structure

---

## Tech Stack

- Python 3.x
- python-binance
- Streamlit
- argparse
- logging
- python-dotenv

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   ├── sample_market_order.log
│   └── sample_limit_order.log
│
├── cli.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your_repository_url>
cd trading_bot
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

---

## Binance Futures Testnet

Register and generate API credentials here:

https://testnet.binancefuture.com

---

# Running the Application

## CLI Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

---

## Streamlit Frontend

Run the Streamlit application:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser automatically.

---

## Logging

Application logs are stored in:

```text
logs/
```

The logs contain:

- Order request details
- API responses
- Error messages
- Timestamps

---

## Sample Output

```text
========== ORDER SUMMARY ==========
Symbol      : BTCUSDT
Side        : BUY
Type        : MARKET
Quantity    : 0.001

========== RESPONSE ==========
Order ID    : 123456789
Status      : FILLED
ExecutedQty : 0.001
Avg Price   : 65000.00

Order placed successfully.
```

---

## Validation and Error Handling

The application validates:

- BUY / SELL order side
- MARKET / LIMIT order type
- Quantity greater than zero
- Price requirement for LIMIT orders
- Binance API exceptions
- Network and unexpected errors

---

## Assumptions

- User has a Binance Futures Testnet account
- API credentials are valid
- Binance Futures Testnet is available
- Quantity precision follows Binance rules

---

## Future Improvements

- Stop-Limit orders
- Order cancellation support
- Position tracking dashboard
- Docker support
- CI/CD pipeline integration
- Database logging
- WebSocket live price updates

---
## Deployment Note

The Streamlit frontend works correctly in local environments.

Deployment on Streamlit Cloud may face Binance regional restrictions because Binance blocks certain cloud-hosted IP ranges.

## Screen shot

<img width="1919" height="1031" alt="image" src="https://github.com/user-attachments/assets/647cca11-2df6-4179-8f44-51aa48b16e08" />


## Author

Balashanmugam R
