# 🧪 DBT Workspace

This folder contains all work related to the **DBT (Data Build Tool)** portion of the project.

DBT is used here to transform raw ingested data into clean, structured tables using SQL-based models that follow modern data warehousing best practices.

## 📁 Folder Structure

- `data-modelling/`  
  Contains **ERD diagrams** and documentation that define the final data warehouse schema in Snowflake.  
  This includes star and snowflake schema elements, key relationships, and model structure.

- `dbt_tools/`  
  Contains the actual **DBT models**, organized by:
  - `staging/`: Clean and standardize raw data from the source layer.
  - `final/`: Build dimension and fact tables for analytics use, based on the structure defined in the ERD.

## 🔍 Purpose

This DBT workspace is designed to:

- Cleanse and transform raw e-commerce data.
- Build a warehouse schema aligned with dimensional modeling principles.
- Document transformation logic clearly and reproducibly.

> 📌 Note: This folder is specific to DBT work. Other tools such as Spark, Kafka, or Airflow will be organized in separate top-level folders in this repository.

## 🧭 Reference

- 📌 [ERD Reference](./data-modelling/ERD.png)
- 📂 [DBT Models](./dbt_tools/)