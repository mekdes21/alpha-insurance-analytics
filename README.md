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

A/B Hypothesis Testing with SumInsured

Hypothesis Testing Goals:

Assess risk and profitability differences using SumInsured.
Metrics:

KPI: SumInsured.
Results Summary:

Provinces and zip codes show significant differences in risk.
Gender and profit margins do not show significant differences.
Business Impact:

Focus marketing strategies on high-risk provinces.
Optimize risk management policies in high-risk zip codes.
Gender-specific policies may not be necessary.


Statistical Modeling

### **Objective**
Analyze and predict `TotalPremium` and `TotalClaims` using statistical modeling techniques.

---

### **Steps Followed**

1. **Data Preparation**  
   - Handled missing data using imputation.  
   - Engineered new features like `VehicleAge` and `SumInsuredPerDoor`.  
   - Encoded categorical data using label encoding and one-hot encoding.  
   - Split the data into training and test sets (70:30 ratio).  

2. **Model Building**  
   - Implemented Linear Regression, Random Forest, and XGBoost models.  
   - Evaluated models based on **Mean Squared Error (MSE)** and **R2-Score**.  

3. **Model Evaluation**  
   - Linear Regression: Baseline comparison.  
   - Random Forest: Improved accuracy through ensemble learning.  
   - XGBoost: Achieved the best performance for premium prediction.  

4. **Feature Importance**  
   - Used SHAP values to interpret the impact of features on predictions.  

- **Key Features:** `VehicleAge`, `SumInsuredPerDoor`, and `Province`.  
- **Recommendation:** Use XGBoost for final predictions due to its superior accuracy.
