import matplotlib.pyplot as plt
import numpy as np
import joblib


def plot_feature_importance(model_file, feature_names):
    """
    Function to plot feature importance based on trained models.
    """
    # Load Model
    model = joblib.load(model_file)

    # Check if the model supports feature importance
    if hasattr(model, "feature_importances_"):
        importance = model.feature_importances_
        indices = np.argsort(importance)[::-1]  # Sort features by importance

        # Plot Feature Importance
        plt.figure(figsize=(10, 6))
        plt.title("Feature Importance")
        plt.bar(range(len(feature_names)), importance[indices], align="center")
        plt.xticks(range(len(feature_names)), np.array(feature_names)[indices], rotation=45)
        plt.xlabel('Features')
        plt.ylabel('Importance')
        plt.tight_layout()
        plt.show()
    else:
        print("Feature importance not available for this model.")


# Example Execution
if __name__ == "__main__":
    feature_names = [
        'SumInsured', 'CalculatedPremiumPerTerm', 'ExcessSelected',
        'Cylinders', 'cubiccapacity', 'kilowatts', 'NumberOfDoors'
    ]

    # Test with Random Forest Model
    model_file = '../reports/models/random_forest.pkl'
    plot_feature_importance(model_file, feature_names)


