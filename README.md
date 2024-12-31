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