# 📦 Sources

This folder serves as the **central source directory** for all raw or generated datasets used by various data engineering tools in this project.

## 📁 Subfolder Structure

- `dbt/`  
  Contains Python scripts to generate **dummy e-commerce data** for DBT modeling. The data simulates realistic entities such as products, categories, customers, and order transactions.

## 📂 Folder Contents

The `sources/` folder can include:

- `.py` files for programmatically generating data (e.g., using Faker)
- `.csv` files as output or static datasets
- Other formats such as `.json`, `.parquet`, etc., depending on the needs of each tool

## 🧭 Purpose

The purpose of this folder is to:

- Provide raw input data that can be ingested into cloud storage or other data platforms (e.g., data warehouses, relational databases, NoSQL stores)
- Support transformation workflows in DBT, Spark, and other tools
- Enable easy expansion by adding new datasets as the project evolves

## 🔗 Related

- 📥 [Ingestion](../ingestion/) – Uploads files from this folder to Amazon S3 as part of the ingestion process
- 🧪 [DBT Models](../dbt/dbt_tools/) – Uses the generated datasets for staging, dimension, and fact models