import argparse

from bot.orders import place_order
from bot.validators import validate_order


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        validate_order(
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        response = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n========== ORDER SUMMARY ==========")
        print(f"Symbol      : {args.symbol}")
        print(f"Side        : {args.side}")
        print(f"Type        : {args.type}")
        print(f"Quantity    : {args.quantity}")

        if args.price:
            print(f"Price       : {args.price}")

        print("\n========== RESPONSE ==========")
        print(f"Order ID    : {response.get('orderId')}")
        print(f"Status      : {response.get('status')}")
        print(f"ExecutedQty : {response.get('executedQty')}")

        if response.get("avgPrice"):
            print(f"Avg Price   : {response.get('avgPrice')}")

        print("\nOrder placed successfully.")

    except Exception as e:

        print(f"\nOrder failed: {str(e)}")

    except Exception as e:

        print(f"\nOrder failed: {str(e)}")
        
if __name__ == "__main__":
    main()