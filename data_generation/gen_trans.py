import pandas as pd
import random
from datetime import datetime, timedelta

NUM_TRANSACTIONS = 50000

TICKERS = [
    "AAPL","TSLA","MSFT","GOOGL","AMZN",
    "NVDA","META","NFLX","AMD","INTC"
]

def generate_transactions():
    data = []
    base_time = datetime.now()

    for i in range(NUM_TRANSACTIONS):
        txn_id = f"T{i}"

        customer_id = random.choice(
            [f"C{random.randint(0, 999)}", "C9999"]  # invalid ID
        )

        ticker = random.choice(TICKERS)

        quantity = random.choice([1, 5, 10, 0, -3])  # invalid cases
        price = random.choice([100, 200, 300, -50])  # invalid cases

        timestamp = random.choice([
            base_time - timedelta(minutes=random.randint(0, 1000)),
            "invalid_time"
        ])

        txn_type = random.choice(["BUY", "SELL"])  # 🔥 NEW FIELD

        data.append([
            txn_id, customer_id, ticker,
            quantity, price, timestamp, txn_type
        ])

    df = pd.DataFrame(data, columns=[
        "txn_id", "customer_id", "ticker",
        "quantity", "price", "timestamp", "txn_type"
    ])

    # duplicates
    df = pd.concat([df, df.sample(200)])

    df.to_csv("data/transactions.csv", index=False)
    print("transactions.csv created")


if __name__ == "__main__":
    generate_transactions()