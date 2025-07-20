# 🛠️ DBT Models

This directory contains all DBT models used to transform raw e-commerce data into structured, analysis-ready tables.

All models are developed based on the **Entity-Relationship Diagram (ERD)** located in `../data-modelling/ERD.png`. The ERD outlines the dimensional schema implemented in the Snowflake data warehouse.

---

## 📁 Folder Structure

- `staging/`  
  Contains staging models used to clean, cast, and rename columns from raw source data. These models prepare the data for transformation into final models.

- `final/`  
  Contains the final fact and dimension tables (e.g., `dim_customers`, `fct_orders`). These are the tables used for analytics and reporting, aligned with the ERD.

---

## 📌 Modeling Approach

- The data model follows a hybrid approach combining **star** and **snowflake** schemas.
  - Example of star: `fct_orders` → `dim_customers`
  - Example of snowflake: `fct_orders_items` → `dim_products` → `dim_categories`
- This structure balances simplicity for reporting with normalization where appropriate.

---

## 🔁 Data Flow

Raw Data → `staging/` (cleaned + standardized) → `final/` (fact + dimension models)

---

## 📚 Related

- 📌 [ERD Reference](../data-modelling/ERD.png) — Entity and relationship overview.