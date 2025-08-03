import pandas as pd

def load_data(file_path)-> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    return pd.read_csv(file_path)

def save_data(df: pd.DataFrame, file_path: str) -> None:
    """
    Save a pandas DataFrame to a CSV file.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    file_path (str): The path where the DataFrame will be saved.
    """
    df.to_csv(file_path, index=True)
