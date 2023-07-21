import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluate_model(model, X, y):
    """
    Evaluate the performance of the sales forecasting model using metrics like MAE and RMSE.
    
    Args:
        model: The trained sales forecasting model.
        X (pd.DataFrame): The input features for evaluation.
        y (pd.Series): The target variable for evaluation.
        
    Returns:
        dict: A dictionary of evaluation metrics.
    """
    predictions = model.predict(X)
    mae = mean_absolute_error(y, predictions)
    rmse = np.sqrt(mean_squared_error(y, predictions))
    
    evaluation_metrics = {
        'MAE': mae,
        'RMSE': rmse
    }
    
    return evaluation_metrics
