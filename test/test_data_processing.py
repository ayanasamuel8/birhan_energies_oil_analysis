import pandas as pd
import numpy as np
import pytest
import sys
from pathlib import Path

# This allows the test script to find the 'src' directory
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import data_processing

@pytest.fixture
def mock_csv_file(tmp_path):
    """
    This is a pytest "fixture". It creates a temporary, fake CSV file
    before a test runs. This makes our test self-contained and reliable.
    """
    file_path = tmp_path / "mock_prices.csv"
    data = {
        "Date": ["20-May-22", "21-May-22", "22-May-22"],
        "Price": [100.0, 102.0, 99.0]
    }
    pd.DataFrame(data).to_csv(file_path, index=False)
    return str(file_path)

def test_load_and_prepare_data_success(mock_csv_file):
    """
    Test the "happy path": Does the function work correctly with valid data?
    """
    # WHEN we call our function on the fake CSV file
    processed_df = data_processing.load_and_prepare_data(mock_csv_file)

    # THEN we assert that the output is what we expect
    assert isinstance(processed_df, pd.DataFrame)
    assert isinstance(processed_df.index, pd.DatetimeIndex)
    assert 'Log_Return' in processed_df.columns
    assert pd.isna(processed_df['Log_Return'].iloc[0])
    
    # Check if the log return calculation is correct
    expected_log_return = np.log(102.0 / 100.0)
    assert np.isclose(processed_df['Log_Return'].iloc[1], expected_log_return)

def test_load_and_prepare_data_file_not_found():
    """
    Test the "sad path": Does the function handle a missing file gracefully?
    """
    # WHEN we call our function with a path that doesn't exist
    result = data_processing.load_and_prepare_data("path/does/not/exist.csv")

    # THEN we assert that the function returns None, as we designed it to
    assert result is None