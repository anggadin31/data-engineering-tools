{{
    config(
        materialized='incremental',
        unique_key=['order_id', 'product_key'],
        incremental_strategy='merge'
    )
}}

WITH orders AS (
    SELECT
        order_id,
        product.product_key,
        quantity,
        price,
        discount,
        net AS final_price,
        shipping_status,
        shipping_cost,
        updated_at
    FROM {{ ref('stg_orders') }} orders
    LEFT JOIN {{ ref('dim_products') }} product
    USING (product_name)
)
SELECT * FROM orders
{% if is_incremental() %}
WHERE orders.updated_at >= (SELECT MAX(this.updated_at) FROM {{ this }} AS this)
{% endif %}
ORDER BY order_id