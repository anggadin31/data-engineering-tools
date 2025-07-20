# Data Engineering Tools

This repository is a personal learning playground for exploring essential tools in the Data Engineering ecosystem.

## 📁 Project Structure

```
data-engineering-tools/
│
├── dbt/
│ ├── data-modelling/ # Contains ERD diagrams and documentation of the Snowflake data warehouse schema
│ └── dbt_tools/ # DBT models, including staging, dimension, fact, and final models
│
├── ingestion/
│ ├── dbt/ # SQL scripts to prepare Snowflake (warehouse, schema creation, and COPY from S3)
│ └── upload_to_s3.py # Python script to upload generated data to Amazon S3
│
├── sources/
│ └── dbt/ # Python scripts for generating dummy e-commerce datasets
│
├── .gitignore # Git ignore rules (e.g., exclude venv, *.csv files, etc.)
└── requirements.txt # Python dependencies required for the project
```

## 🧰 Tools Covered

| Tool        | Status     |
|-------------|------------|
| DBT         | ✅ Implemented |
| Apache Spark   | ⏳ Coming soon |
| Hadoop         | ⏳ Coming soon |
| Apache Kafka   | ⏳ Coming soon |

## 🚀 Getting Started

```bash
git clone https://github.com/anggadin31/data-engineering-tools.git
cd data-engineering-tools
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 📌 Notes

This project is under active development as a personal study repository. Expect rapid iterations and ongoing changes.
