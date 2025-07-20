SELECT
    DISTINCT
    {{ dbt_utils.generate_surrogate_key(['product_name']) }} AS product_key,
    category.category_key,
    product_name
FROM {{ ref('stg_products') }} products
LEFT JOIN {{ ref('dim_categories') }} category
    USING (category)