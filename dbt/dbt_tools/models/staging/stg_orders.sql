SELECT
    order_id,
    date AS order_date,
    member_id AS customer_id,
    items AS product_name,
    quantity,
    price,
    net,
    "payment method" AS payment_method,
    shipping_address,
    "shipping cost" AS shipping_cost,
    "shipping status" AS shipping_status,
    discount,
    updated_at
FROM {{ source('raw_orders', 'orders') }}
ORDER BY date