{%- macro test_expect_positive(model, column_name) -%}
SELECT *
FROM {{ model }}
WHERE {{ column_name }} <= 0
{%- endmacro -%}