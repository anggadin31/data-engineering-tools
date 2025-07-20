---

## 🌐 Ingestion Flow Overview

The ingestion flow is designed to simulate a real-world cloud data pipeline:

1. **Python script (`upload_to_s3.py`)**  
   - Uploads generated CSV files to an Amazon S3 bucket.
   - This simulates the scenario where data lands in cloud storage from upstream systems.

2. **SQL scripts (`dbt/` folder)**  
   - Contains Snowflake SQL used to:
     - Create necessary databases and schemas.
     - Create external or internal tables.
     - Perform `COPY INTO` operations from S3 to Snowflake tables.

By designing the ingestion this way, the project mimics a full **cloud-native ETL pipeline**, where Snowflake acts as the central warehouse and S3 is the data lake or landing zone.

---

## 📁 Folder Structure

- `upload_to_s3.py`  
  Python script to upload raw CSV files to Amazon S3. Handles credential setup, error handling, and object naming.

- `dbt/`  
  Contains SQL scripts to:
  - Create Snowflake database and schema
  - Prepare ingestion tables
  - Perform `COPY INTO` commands to load data from S3

---

## ⚙️ Why This Approach?

By uploading to S3 and then using Snowflake's `COPY INTO`, this project intentionally avoids local data loads. It reflects the **best practice** in modern data engineering where cloud storage acts as a reliable, scalable, and decoupled ingestion layer.

---

## 📦 Related

- 🔗 [sources/](../sources/) — Code that generates the raw CSV files.
- 🔗 [dbt/](../dbt/) — DBT transformations applied after ingestion.