# 🧪 Data Sources (Synthetic Generator)

This directory contains Python scripts used to generate **synthetic raw data** for the simulated e-commerce platform.

---

## 📌 Purpose

The scripts in this folder create raw `.csv` files that emulate transactional and dimensional data, such as:

- Customers  
- Products and Categories  
- Orders and Order Items  

The generated data is intentionally "raw" and not yet structured for analytics. This allows us to simulate the full journey from **unstructured input → cloud ingestion → warehouse modeling**.

---

## 🛠 How It Works

- The Python files use the `Faker` library and other randomization logic to produce realistic but fake e-commerce datasets.
- Output is written as CSV files into the same directory, e.g., `ecommerce_orders.csv`, `customers.csv`, etc.

These files are not meant to be version-controlled and should be excluded using `.gitignore`.

---

## 🔄 Relationship with Ingestion

Once data is generated here:

1. The ingestion pipeline (in [`ingestion/`](../ingestion/)) picks up the CSV files.
2. Files are uploaded to Amazon S3 using the `upload_to_s3.py` script.
3. Snowflake then performs `COPY INTO` operations to load the data into warehouse staging tables.

This simulates a **cloud-native data pipeline** where raw data lands in S3 and is later transformed using DBT.

---

## 🧾 Notes

- These scripts are **deterministic enough** to support repeatable tests but still introduce randomness to simulate real-world variability.
- Make sure to regenerate the data if schema changes are made in the DBT models.

---

## 📦 Related

- 🔗 [ingestion/](../ingestion/) — Uploads this data to S3 and performs ingestion into Snowflake.
- 🔗 [dbt/](../dbt/) — Transformations and modeling of the ingested data.