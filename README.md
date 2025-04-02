# Sports Business Intelligence Platform
The Sports Business Intelligence Platform is a comprehensive end-to-end solution designed to empower sports organizations with deep insights into their operations, fan engagement, and market dynamics. By integrating data engineering, advanced analytics, and machine learning, this project delivers actionable KPIs, predictive forecasts, and performance benchmarks to drive strategic decision-making.

## Project Overview
This project is built on a modular architecture that encompasses several key components:

## ETL Pipeline:
A robust pipeline that extracts raw data from CSV files, transforms and cleans it, and loads it into a local SQLite database. This pipeline is designed for easy migration to cloud data warehouses like BigQuery or Redshift.

## KPI Reporting:
A suite of SQL queries that generate critical metrics—such as daily ticket sales, revenue breakdowns, and user engagement figures—that serve as the backbone for business intelligence and dashboard visualizations.

## Machine Learning & Forecasting:
Advanced models forecast key performance indicators using time-series method (Prophet) and predict user churn using XGBoost. Additional segmentation via clustering (KMeans) offers insights into fan behavior. All models are tracked using MLflow for experiment reproducibility.

## Cloud-Ready Architecture:
The entire solution is designed with scalability in mind. While the initial development and testing are performed locally, the system can be seamlessly migrated to cloud platforms such as GCP (BigQuery, Vertex AI) or AWS (Redshift, SageMaker). CI/CD pipelines using GitHub Actions ensure smooth integration and deployment.

## CI/CD with GitHub Actions
A CI/CD pipeline is configured using GitHub Actions (see .github/workflows/ci.yml). This pipeline runs your ETL process, SQL queries, and ML model scripts automatically on pushes and pull requests to the main branch.

## Cloud Deployment
This solution is built to be cloud-ready. You can easily migrate the local ETL workflow and models to cloud platforms:

### Google Cloud Platform (GCP):
Use Google Cloud Storage for data, BigQuery for warehousing, and Vertex AI for model deployment.

### Amazon Web Services (AWS):
Use S3 for data storage, Redshift as your data warehouse, and SageMaker for ML model deployment.

Automated deployment and monitoring can be configured using GitHub Actions, Cloud Build, or AWS CodePipeline.
