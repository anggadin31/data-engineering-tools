SELECT
    DISTINCT
    {{ dbt_utils.generate_surrogate_key(['category']) }} AS category_key,
    category
FROM {{ ref('stg_products') }}