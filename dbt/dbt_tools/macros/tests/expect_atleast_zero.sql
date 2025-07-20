{%- macro test_expect_at_least_zero(model, column_name) -%}
SELECT *
FROM {{ model }}
WHERE {{ column_name }} < 0
{%- endmacro -%}