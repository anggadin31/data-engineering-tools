# 🧩 Data Modeling Overview

This folder contains the Entity-Relationship Diagram (ERD) used to model the Snowflake data warehouse for the e-commerce analytics project.

The modeling approach follows dimensional modeling best practices using a **star schema**. It separates **dimensions** (the "who", "what", and "where") from **fact tables** (the "what happened"). This enables scalable, performant analytical queries.

---

## 📐 ERD Structure

The ERD (`ERD.png`) includes the following tables and relationships:

### 🟦 Dimension Tables

#### `dim_categories`
- `category_key` (PK): Unique identifier for category
- `category`: Category name (e.g., Electronics, Apparel)

#### `dim_products`
- `product_key` (PK): Unique identifier for product
- `category_key` (FK): Links to `dim_categories`
- `product_name`: Product name

#### `dim_customers`
- `customer_id` (PK): Unique customer ID
- `customer_name`: Full name
- `email`: Contact email
- `phone`: Contact number
- `updated_at`: Timestamp for slowly changing dimension (SCD)

---

### 🟥 Fact Tables

#### `fct_orders`
- `order_id` (PK): Unique order ID
- `customer_id` (FK): Links to `dim_customers`
- `order_date`: Date and time of the order
- `order_stats`: Order status (e.g., completed, returned)
- `payment_method`: Payment type (e.g., credit card)
- `total_amount`: Total value of the order
- `total_order_returned`: Count of items returned
- `updated_at`: For audit/history purposes

#### `fct_orders_items`
- `order_id` (FK): Links to `fct_orders`
- `product_key` (FK): Links to `dim_products`
- `quantity`: Number of units ordered
- `price`: Base price per unit
- `discount`: Discount percentage applied
- `final_price`: Net price after discount
- `shipping_cost`: Cost of delivery
- `shipping_status`: Status of shipment (e.g., shipped, delayed)
- `updated_at`: Change tracking

---

## 🔗 Relationships

- `fct_orders.customer_id` → `dim_customers.customer_id`
- `fct_orders_items.order_id` → `fct_orders.order_id`
- `fct_orders_items.product_key` → `dim_products.product_key`
- `dim_products.category_key` → `dim_categories.category_key`

These many-to-one relationships ensure referential integrity and enable drill-down analysis (e.g., sales by category, revenue per customer).

---

## 🧠 Why This Matters

This data model is designed to support:
- Time-based analysis (e.g., daily revenue trends)
- Customer behavior insights
- Product performance tracking
- Operational reporting (returns, shipping, etc.)

It is optimized for use in analytics tools and supports transformations using DBT.