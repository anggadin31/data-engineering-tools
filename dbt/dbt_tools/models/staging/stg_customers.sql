WITH
latest_customers AS (
    SELECT
        member_id AS customer_id,
        customer AS customer_name,
        REGEXP_REPLACE(email, '\\s+', '') AS email,
        "phone number" AS phone,
        date AS updated_at,
        ROW_NUMBER() OVER (
            PARTITION BY member_id
            ORDER BY date DESC
        ) AS row_num
    FROM {{ source('raw_orders', 'orders') }}
)
SELECT * FROM latest_customers
WHERE row_num = 1