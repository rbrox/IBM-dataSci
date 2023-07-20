import pandas as pd
import numpy as np

def test():
    print('Test')
    

def load_data(path = './data/'):
    # Path is the relative file path to the data folder, defaults to data
    """
    Loads the data required .
    
    Returns:
        pd.DataFrame: The loaded data.
    """
    # Load the necessary datasets
    train_data = pd.read_csv( path + 'train.csv')
    test_data = pd.read_csv(path + 'test.csv')
    stores_data = pd.read_csv(path + 'stores.csv')
    oil_data = pd.read_csv(path + 'oil.csv')
    holidays_data = pd.read_csv(path + 'holidays_events.csv')
    
    # Return the loaded data
    return train_data, test_data, stores_data, oil_data, holidays_data

def assess_data(data):
    """
    Report on data health
    """
    df = pd.DataFrame(data)
    
    # columns 
    columns = list(df.columns)
    print(columns)
    
    # dtypes 
    dtypes = dict(df.dtypes)
    print(dtypes)
    
    # dtypes of object type
    object_columns = []
    for col in dtypes:
        if dtypes[col] == 'dtype('O')'
            object_columns.append(col)
    
    print(object_columns)
    
def handle_missing_values(data):
    """
    Handle missing values in the data.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: The DataFrame with missing values handled.
    """
    # Implement logic to handle missing values (e.g., imputation or removal)
    pass

def feature_engineering(data):
    """
    Perform feature engineering transformations on the data.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: The DataFrame with feature engineering transformations applied.
    """
    # Implement logic for feature engineering (e.g., date transformations, categorical encoding, new feature creation)
    pass

def preprocess_data(data):
    """
    Preprocess the data by applying necessary preprocessing steps.
    
    Args:
        data (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    data = handle_missing_values(data)
    data = feature_engineering(data)
    # Apply any additional preprocessing steps
    return data

if __name__ == '__main__': 
    test()