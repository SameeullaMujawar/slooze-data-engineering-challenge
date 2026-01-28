# Slooze Data Engineering Take Home Challenge

## Overview
This project implements an end-to-end data collection and analysis pipeline for electronics products from a marketplace-style data source.

## Part A – Data Collection
A custom Python data gathering script was built to extract product data across multiple electronics categories using a public product catalog API.

Collected fields:
- Product Name
- Price
- Supplier (simulated multiple vendors)
- Location
- Category

Data stored in CSV format.

## Part B – Exploratory Data Analysis (EDA)
EDA was performed using pandas, matplotlib, and seaborn to analyze:

- Product distribution by category
- Price trends and distribution
- Popular product types
- Average price comparison

## Key Insights
- Laptops have higher average prices than smartphones
- Smartphones have higher listing volume
- Significant price variation exists within each category
- Market shows demand concentration around specific models

## How to Run

### Install dependencies
pip install -r requirements.txt

### Collect data
python scraper.py

### Run EDA
jupyter notebook eda.ipynb

## Challenges & Approach
Major B2B marketplaces implement heavy anti-bot protections. To ensure reliability and respectful data collection, a publicly accessible product feed was integrated as a data source, simulating a marketplace ingestion pipeline.

## Technologies Used
Python, Requests, Pandas, Matplotlib, Seaborn


## Future Improvements

• Add pagination for larger datasets
• Store data in database (PostgreSQL)
• Automate ETL pipeline
• Add more product categories