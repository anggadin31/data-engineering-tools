CREATE TABLE raw_dbt.shop.orders
( id INTEGER PRIMARY KEY AUTOINCREMENT ORDER,
  date TIMESTAMP,
  customer VARCHAR (250),
  items VARCHAR (250),
  quantity INTEGER,
  price INTEGER,
  total INTEGER,
  email VARCHAR (250),
  "phone number" INTEGER,
  category VARCHAR (250),
  "payment method" VARCHAR (250),
  shipping_address VARCHAR (250),
  "shipping cost" INTEGER,
  "shipping status" VARCHAR (250),
  discount FLOAT,
  ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE analytics_dbt.dbt_learning.dim_customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT ORDER,
    name VARCHAR(100),
    email VARCHAR(150),
    phone varchar(20)
);

CREATE TABLE analytics_dbt.dbt_learning.dim_category (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT ORDER,
    category VARCHAR(150)
);

CREATE TABLE analytics_dbt.dbt_learning.dim_product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT ORDER,
    category_id INTEGER,
    product_name VARCHAR(150)
);

CREATE TABLE analytics_dbt.dbt_learning.fct_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT ORDER,
    order_date DATETIME,
    customer_id INTEGER,
    total INTEGER,
    payment_method VARCHAR(50),
    order_status VARCHAR(50)
);