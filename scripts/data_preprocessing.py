import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer


def preprocess_data(file_path):
    # Load Dataset
    df = pd.read_csv(file_path, low_memory=False)

    # Debugging - Check data types and missing values
    print("Initial Data Types:\n", df.dtypes)
    print("Missing Values:\n", df.isnull().sum())

    # Drop unnecessary columns
    drop_cols = ['UnderwrittenCoverID', 'PolicyID', 'TransactionMonth', 'Title', 'Language']
    df.drop(columns=drop_cols, inplace=True, errors='ignore')  # Ignore errors if columns are missing

    # Handle Missing Data
    num_imputer = SimpleImputer(strategy='median')   # For numerical columns
    cat_imputer = SimpleImputer(strategy='most_frequent')  # For categorical columns

    # Separate Numerical and Categorical Columns
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns

    # Impute Missing Values
    df[num_cols] = num_imputer.fit_transform(df[num_cols])
    df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

    # Feature Engineering
    df['VehicleAge'] = 2024 - df['RegistrationYear']  # Calculate Vehicle Age
    df['SumInsuredPerDoor'] = df['SumInsured'] / (df['NumberOfDoors'] + 1e-6)  # Avoid divide-by-zero

    # Debugging - Check for new features
    print("New Feature Examples:\n", df[['VehicleAge', 'SumInsuredPerDoor']].head())

    # Encode Categorical Data
    le = LabelEncoder()

    # Example Encoding for Binary Columns
    df['Gender'] = le.fit_transform(df['Gender'])  # Encode Gender as 0/1
    df['IsVATRegistered'] = df['IsVATRegistered'].astype(int)  # Convert boolean to int

    # One-Hot Encoding for Multi-Class Categorical Columns
    df = pd.get_dummies(df, columns=[
        'Province', 'AccountType', 'VehicleType', 'Product', 'CoverCategory', 'CoverType', 'StatutoryRiskType'
    ], drop_first=True)

    # Feature Scaling
    scaler = StandardScaler()
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[num_cols] = scaler.fit_transform(df[num_cols])  # Normalize numerical features

    # Train-Test Split
    X = df.drop(['TotalPremium', 'TotalClaims', 'CustomValueCategory'], axis=1, errors='ignore')
    y = df['TotalPremium']  # Target Variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Debug Shapes
    print("X_train Shape:", X_train.shape)
    print("y_train Shape:", y_train.shape)
    print("X_test Shape:", X_test.shape)
    print("y_test Shape:", y_test.shape)

    return X_train, X_test, y_train, y_test


