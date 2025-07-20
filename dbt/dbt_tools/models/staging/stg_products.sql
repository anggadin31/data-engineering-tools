SELECT
    DISTINCT
    items AS product_name,
    category
FROM {{ source('raw_orders', 'orders') }}
ORDER BY items
