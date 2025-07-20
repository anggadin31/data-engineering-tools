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