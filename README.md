# alpha-insurance-analytics
# Insurance Analytics - Task 1

This repository contains the analysis for Task 1: Exploratory Data Analysis (EDA) on insurance claims and premiums.

## Folder Structure:
- data/: Contains raw and processed data.
- notebooks/: Jupyter notebooks for EDA steps.
- scripts/: Python scripts for reusable functions.
- reports/: Summary reports and visualizations.

## Setup
1. Clone the repository:
   git clone https://github.com/mekdes21/alpha-insurance-analytics

2. Install dependencies:
   pip install -r requirements.txt

3. Open Jupyter Notebooks:
   jupyter notebook

4. ## Data Version Control (DVC)

This project uses **DVC** (Data Version Control) to manage large datasets and model files efficiently. DVC allows us to track, version, and share datasets, making collaboration easier while keeping Git repositories lightweight.

### Key Concepts:
- insurance_data are tracked by DVC rather than Git to handle large datasets.
- DVC stores the metadata and versioning of the data, while actual data files are stored in remote storage (e.g., AWS S3, Google Drive).
A/B Hypothesis Testing
Overview
This project conducts A/B hypothesis testing to evaluate the impact of key features on risk and profit margins across different groups in insurance claims data. The primary objective is to optimize marketing strategies, identify low-risk clients, and predict claim behavior effectively.

1. A/B Testing Goals
The following Null Hypotheses (H0) were tested:

Province Risk Differences: There are no significant risk differences across provinces.
Zip Code Risk Differences: There are no significant risk differences between zip codes.
Zip Code Profit Margins: There are no significant margin differences between zip codes.
Gender Risk Differences: There are no significant risk differences between Women and Men.
2. Metrics Selected
Key Performance Indicators (KPIs)
Risk Assessment: Measured by the average number of claims filed and claim amounts (TotalClaims).
Profit Margins: Evaluated using the average premium collected minus claims paid (Margin).
3. Data Segmentation
Group A (Control Group): Plans without specific features (e.g., Male, Low-Risk Provinces).
Group B (Test Group): Plans with the feature under testing (e.g., Female, High-Risk Provinces).

Segmentation Examples:
Gender: Split into Male and Female.
Province: Divided based on risk levels determined through clustering or analysis.
Zip Codes: Grouped into high and low claim areas based on median values.
4. Statistical Testing
Tests Conducted:

Chi-Squared Test: For categorical variables such as gender and risk category.
t-Test or z-Test: For numerical variables like claim amounts and profit margins.
Significance Level:

p-value < 0.05 - Reject the null hypothesis (statistically significant).
p-value ≥ 0.05 - Fail to reject the null hypothesis (not significant).

