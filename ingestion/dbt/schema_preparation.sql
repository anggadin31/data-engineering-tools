CREATE WAREHOUSE so_warehouse WITH WAREHOUSE_SIZE = xsmall;
CREATE DATABASE raw_dbt;
CREATE DATABASE analytics_dbt;
CREATE SCHEMA raw_dbt.shop;
CREATE SCHEMA analytics_dbt.dbt_learning;