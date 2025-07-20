SELECT
    customer_id,
    customer_name,
    email,
    phone,
    updated_at,
FROM {{ ref('stg_customers') }}