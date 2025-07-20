COPY INTO raw_dbt.shop.orders (date,customer,items,quantity,price,total,email,"phone number",category,"payment method",shipping_address,"shipping cost","shipping status",discount)
FROM 's3://personal-project-learning-data/data-dbt/ecommerce_dummy_data.csv'
file_format = (
    TYPE = 'CSV'
    FIELD_DELIMITER = ','
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    SKIP_HEADER = 1
    TIMESTAMP_FORMAT = 'YYYY-MM-DD"T"HH24:MI:SS'
    );