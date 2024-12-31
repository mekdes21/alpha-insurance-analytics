import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Model Training Function
def train_models(X_train, X_test, y_train, y_test):
    # Debug: Shape of Data
    print("X_train Shape:", X_train.shape)
    print("y_train Shape:", y_train.shape)

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    mse_lr = mean_squared_error(y_test, y_pred_lr)
    r2_lr = r2_score(y_test, y_pred_lr)
    print("Linear Regression - MSE:", mse_lr, "R2:", r2_lr)
    joblib.dump(lr, '../reports/models/linear_regression.pkl')

    # Random Forest
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)
    print("Random Forest - MSE:", mse_rf, "R2:", r2_rf)
    joblib.dump(rf, '../reports/models/random_forest.pkl')

    # Decision Tree
    dt = DecisionTreeRegressor(random_state=42)
    dt.fit(X_train, y_train)
    y_pred_dt = dt.predict(X_test)
    mse_dt = mean_squared_error(y_test, y_pred_dt)
    r2_dt = r2_score(y_test, y_pred_dt)
    print("Decision Tree - MSE:", mse_dt, "R2:", r2_dt)
    joblib.dump(dt, '../reports/models/decision_tree.pkl')

    # Return Results
    return {
        'Linear Regression': {'MSE': mse_lr, 'R2': r2_lr},
        'Random Forest': {'MSE': mse_rf, 'R2': r2_rf},
        'Decision Tree': {'MSE': mse_dt, 'R2': r2_dt}
    }


# Main Execution
if __name__ == "__main__":
    # Load Data
    df = pd.read_csv("../data/insurance_data_cleaned.csv")  
    
    # Feature Selection
    features = [
        'SumInsured', 'CalculatedPremiumPerTerm', 'ExcessSelected',
        'Cylinders', 'cubiccapacity', 'kilowatts', 'NumberOfDoors'
    ]
    target = 'TotalPremium'

    # Handle 'ExcessSelected' Column
    df['ExcessSelected'] = df['ExcessSelected'].replace({
        'No excess': 0,
        'Low': 1,
        'Medium': 2,
        'High': 3
    })

    # Ensure all data is numeric and replace NaN values
    X = df[features].select_dtypes(include=[np.number])  # Select only numeric columns
    X = X.fillna(0)  # Replace NaN with 0
    y = df[target]

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Models
    results = train_models(X_train, X_test, y_train, y_test)

    # Print Results
    print(results)


