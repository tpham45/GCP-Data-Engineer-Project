# NYC Yellow Taxi Data Analytics Project

## Introduction
This project showcases real-world taxi data analytics centered around New York City. Utilizing a range of tools, including GCP Services, Python, Virtual Machine, and Mage Data Pipeline, we prepare data for insightful analysis. The findings are visualized using PowerBI and Looker Studio to inform data-driven decisions.

## Architecture Framework
![Architecture Diagram](https://github.com/tpham45/Taxi_Analytics/blob/main/Data%20Analytic%20Uber/ERD%20Diagram/architecture.jpg)

## Technology Stack
- **Programming Language**: Python
- **Google Cloud Platform (GCP)**:
  - Google Storage
  - Compute Engine (VM Instance)
  - BigQuery
  - Looker Studio
- **Data Pipeline Tool**: [Mage-AI](https://www.mage.ai/)
- **Data Visualization**: Power BI & Looker Studio

## Data Source
We utilize the TLC Trip Record Data, which encompasses a wealth of information from yellow and green taxi trip records, including pick-up and drop-off times, locations, distances, fares, and more. These datasets have been provided under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP).

- **Minimized Dataset Sample**: [Download Here](https://github.com/tpham45/Taxi_Analytics/blob/main/Data%20Analytic%20Uber/Data%20Source/yellow_tripdata_2023-11(cut)1.csv)

### Additional Resources
- [TLC Trip Record Data Website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [Data Dictionary PDF](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

## ERD Diagram
![ERD Diagram](https://github.com/tpham45/Taxi_Analytics/blob/main/Data%20Analytic%20Uber/ERD%20Diagram/ERD%20Diagram.png)

## Step-by-Step Guide
1. Download the dataset to your local machine. [Dataset Download](https://github.com/tpham45/Taxi_Analytics/blob/main/Data%20Analytic%20Uber/Data%20Source/yellow_tripdata_2023-11(cut)1.csv)
2. Perform preliminary data transformations in Jupyter Notebooks. [Codebase](https://github.com/tpham45/Taxi_Analytics/blob/main/Data%20Analytic%20Uber/Python%20Script/data_transforming.ipynb)
3. Initialize the GCP Console.
4. Create and configure a GCP VM Instance. [Installation Scripts](https://github.com/tpham45/Taxi_Analytics/blob/main/Data%20Analytic%20Uber/Command%20Scripts/command.txt)
5. Upload the dataset to Google Cloud Storage with 'Public Access' settings.
6. Establish a new Mage environment. Refer to [Mage documentation](https://www.mage.ai/) for details.
7. Implement a new firewall rule for Mage project access.
8. Develop the ETL pipeline. [ETL Framework](https://github.com/tpham45/Taxi_Analytics/blob/main/Data%20Analytic%20Uber/Mage_AI/DataPipelineFrameWork/PipelineFrameWork.png)
9. Configure `io_config.yml` for BigQuery data export. (For assistance, contact the support team)
10. Create analytical data products using SQL scripts. [SQL Scripts](https://github.com/tpham45/Taxi_Analytics/blob/main/Data%20Analytic%20Uber/GCP%20BigQuery%20SQL/taxi_analytics_dp.sql)
11. Develop a dashboard in PowerBI or Looker Studio for visualization.

## References
- [Instructional YouTube Video](https://www.youtube.com/watch?v=WpQECq5Hx9g)
