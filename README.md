# 📊 Customer Portfolio Analytics Pipeline (PySpark + AWS S3)

## 🚀 Overview

This project is an end-to-end data engineering pipeline that ingests market data and customer transaction data, processes it using PySpark, and computes portfolio value and profit/loss (PnL) per customer.

The system follows a **Bronze → Silver → Gold** architecture and demonstrates data modeling, data quality enforcement, and analytical transformations.

---

## 🧠 Business Problem

Financial platforms need to answer:

- What is each customer’s portfolio worth?
- Are they making or losing money?
- How is risk distributed across customers?

This pipeline solves that by deriving **portfolio value and PnL** from raw transaction data.

---

## 🏗️ Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/5924a0dc-3461-471b-8af0-a9c68753c4aa" />

<img width="701" height="391" alt="data_lineagede drawio" src="https://github.com/user-attachments/assets/09f95557-eafa-48ad-8635-b996dea7c200" />



---

## 🧱 Data Layers

### 🟤 Bronze Layer (Raw)
- Stock API (JSON)
- Customers, Transactions, Holdings (CSV)
- Stored in S3 as **append-only**
- Partitioned by `load_date`

---

### ⚪ Silver Layer (Cleaned Data)

Transformations:
- Schema normalization (JSON flattening)
- Data quality checks (price > 0, valid timestamps)
- Deduplication
- Referential integrity (valid customer_id, ticker)

Output:
- `customers`
- `transactions`
- `stock_prices`
- `holdings`

---

### 🟡 Gold Layer (Business Logic)

Core logic:
- Convert transactions → net positions
- Compute average buy price (cost basis)
- Fetch latest stock prices using window functions
- Calculate:
  - `portfolio_value`
  - `PnL`
- Aggregate per customer

---

## ⭐ Data Model

- **Fact Tables**
  - Transactions (event-based)
  - Customer Positions (derived)
  - Customer Portfolio (aggregated)

- **Dimensions**
  - Customers
  - Stock Prices

---

## 📈 Key Metrics

- `total_portfolio_value`
- `total_pnl`
- `net_quantity`
- `avg_buy_price`

---

## 🛠️ Tech Stack

- PySpark (Databricks)
- AWS S3 (Data Lake)
- Parquet (storage format)
- Python (data generation + ingestion)

---

## 🔥 Key Concepts Demonstrated

- Event-based modeling (transactions as source of truth)
- Star schema design
- Data quality enforcement
- Window functions (latest stock price)
- Batch pipeline design

---

## ⚠️ Note on Credentials

All AWS credentials and sensitive information have been removed from this repository.

Use environment variables or configuration files for secure access.

---

## 🚀 Future Improvements

- Incremental pipeline (process only new data)
- Athena queries for analytics
- Dashboard (Streamlit / BI tool)
- FIFO/LIFO-based PnL calculation

---

## 👨‍💻 Author

Built as a data engineering project to demonstrate end-to-end pipeline design, modeling, and analytics.

