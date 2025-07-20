{{-
    config(
        materialized='incremental',
        unique_key='order_id',
        incremental_strategy='merge'
    )
-}}
WITH
orders AS (
    SELECT
        order_id,
        order_date,
        customer_id,
        payment_method,
        shipping_status,
        net,
        updated_at
    FROM {{ ref('stg_orders') }}
),
done_returned AS (
    SELECT order_id, COUNT(*) AS order_done
    FROM orders
    WHERE shipping_status IN ('done', 'returned')
    GROUP BY order_id
),
returned AS (
    SELECT order_id, COUNT(*) AS order_returned
    FROM orders
    WHERE shipping_status = 'returned'
    GROUP BY order_id
),
total_orders AS (
    SELECT order_id, COUNT(*) AS total_orders
    FROM orders
    GROUP BY order_id
),
final AS (
    SELECT
        orders.order_id,
        MAX(orders.order_date) AS order_date,
        orders.customer_id,
        orders.payment_method,
        SUM(orders.net) AS total_amount,
        CASE
            WHEN done_returned.order_done = total_orders.total_orders THEN 'done'
            WHEN orders.shipping_status = 'cancelled' THEN 'cancelled'
        ELSE 'in process'
        END AS order_status,
        COALESCE(returned.order_returned, 0) AS total_order_returned,
        MAX(orders.updated_at) AS updated_at
    FROM orders
    LEFT JOIN done_returned
        ON orders.order_id = done_returned.order_id
    LEFT JOIN total_orders
        ON orders.order_id = total_orders.order_id
    LEFT JOIN returned
        ON orders.order_id = returned.order_id
    GROUP BY orders.order_id,
        orders.customer_id,
        orders.payment_method,
        order_status,
        total_order_returned
)
SELECT * FROM final
{% if is_incremental() -%}
WHERE updated_at >= (SELECT MAX(updated_at) FROM {{ this }})
{% endif -%}
ORDER BY order_id