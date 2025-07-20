import pandas as pd
from ingestion.upload_to_s3 import upload
if __name__ == '__main__':
    upload('personal-project-learning-data', 'data-dbt/ecommerce_dummy_data.csv', 'sources/dbt/ecommerce_dummy_data.csv')