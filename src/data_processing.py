"""
Data Processing Module for the Birhan Energies project.

This module contains functions for loading, cleaning, and preparing the
Brent oil price data for analysis. The main function, load_and_prepare_data,
handles the entire workflow from raw CSV to a processed DataFrame.
"""

import pandas as pd
import numpy as np
from typing import Optional

def load_and_prepare_data(file_path: str) -> Optional[pd.DataFrame]:
    """
    Loads the raw Brent oil price data, cleans it, and prepares it for analysis.

    This function performs the following steps:
    1. Loads the data from the specified CSV file path.
    2. Cleans and converts the 'Date' column to datetime objects.
    3. Sets the 'Date' column as the DataFrame index and sorts it.
    4. Calculates the daily log returns and adds it as a new column.

    Args:
        file_path (str): The path to the raw CSV data file.

    Returns:
        Optional[pd.DataFrame]: A processed DataFrame with a datetime index,
                                'Price', and 'Log_Return' columns, or None
                                if the file is not found.
    """
    try:
        # 1. Load the data
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from {file_path}.")

        # 2. Clean and convert the 'Date' column
        # pandas.to_datetime is robust enough to handle the mixed formats.
        # We'll also remove any extra quotes just in case.
        if 'Date' not in df.columns:
            print("Error: 'Date' column not found in the data.")
            return None
            
        df['Date'] = df['Date'].astype(str).str.replace('"', '')
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # Drop rows where date conversion failed
        df.dropna(subset=['Date'], inplace=True)

        # 3. Set the index and sort
        df = df.set_index('Date').sort_index()

        # 4. Calculate log returns
        df['Log_Return'] = np.log(df['Price']).diff()

        print("Data cleaning and preparation complete.")
        return df

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during data processing: {e}")
        return None