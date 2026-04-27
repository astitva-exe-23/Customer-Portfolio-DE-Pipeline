import pandas as pd
import random
from datetime import datetime, timedelta

NUM_CUSTOMERS = 1000
NUM_TRANSACTIONS = 50000
NUM_HOLDINGS = 10000

TICKERS = [
    "AAPL","TSLA","MSFT","GOOGL","AMZN",
    "NVDA","META","NFLX","AMD","INTC"
]

# ----------------------------
# CUSTOMERS
# ----------------------------
def generate_customers():
    data = []

    for i in range(NUM_CUSTOMERS):
        customer_id = f"C{i}"

        name = random.choice(["Alice", "Bob", "Charlie", None])  # nulls
        age = random.choice([25, 30, 40, -5, 200])  # invalid ages
        risk = random.choice(["low", "medium", "high", "unknown"])  # invalid category

        data.append([customer_id, name, age, risk])

    df = pd.DataFrame(data, columns=[
        "customer_id", "name", "age", "risk_profile"
    ])

    # duplicate rows
    df = pd.concat([df, df.sample(50)])

    df.to_csv("data/customers.csv", index=False)
    print("customers.csv created")


# ----------------------------
# TRANSACTIONS
# ----------------------------
def generate_transactions():
    data = []

    base_time = datetime.now()

    for i in range(NUM_TRANSACTIONS):
        txn_id = f"T{i}"

        customer_id = random.choice(
            [f"C{random.randint(0, NUM_CUSTOMERS-1)}", "C9999"]  # invalid ID
        )

        ticker = random.choice(TICKERS)

        quantity = random.choice([1, 5, 10, 0, -3])  # invalid
        price = random.choice([100, 200, 300, -50])  # invalid

        timestamp = random.choice([
            base_time - timedelta(minutes=random.randint(0, 1000)),
            "invalid_time"
        ])

        data.append([
            txn_id, customer_id, ticker, quantity, price, timestamp
        ])

    df = pd.DataFrame(data, columns=[
        "txn_id", "customer_id", "ticker",
        "quantity", "price", "timestamp"
    ])

    # duplicate rows
    df = pd.concat([df, df.sample(200)])

    df.to_csv("data/transactions.csv", index=False)
    print("transactions.csv created")


# ----------------------------
# HOLDINGS
# ----------------------------
def generate_holdings():
    data = []

    for _ in range(NUM_HOLDINGS):
        customer_id = f"C{random.randint(0, NUM_CUSTOMERS-1)}"
        ticker = random.choice(TICKERS + ["FAKE"])  # invalid ticker
        quantity = random.choice([5, 10, 20, -10])  # invalid

        data.append([customer_id, ticker, quantity])

    df = pd.DataFrame(data, columns=[
        "customer_id", "ticker", "quantity"
    ])

    # duplicates
    df = pd.concat([df, df.sample(100)])

    df.to_csv("data/holdings.csv", index=False)
    print("holdings.csv created")


# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    generate_customers()
    generate_transactions()
    generate_holdings()