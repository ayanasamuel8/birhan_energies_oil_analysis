"""
Configuration file for the Birhan Energies project.

This file centralizes all file paths and constants to make the project
more organized and easier to maintain. Instead of hardcoding file paths
in notebooks or scripts, we import them from here.
"""

# --- File Paths ---

# Path to the raw, original Brent oil prices CSV file.
RAW_DATA_PATH = '../data/00_raw/BrentOilPrices.csv'

# Path to the cleaned and processed data file.
# This is the output from the initial data preparation step.
PROCESSED_DATA_PATH = '../data/01_processed/BrentOilPrices_Cleaned.csv'

# Path to the compiled list of major geopolitical and economic events.
EVENTS_DATA_PATH = '../data/compiled/events.csv'

# --- Model Parameters ---
# (We can add model-specific configurations here later if needed)
ANALYSIS_START_DATE = '2005-01-01'
ANALYSIS_END_DATE = '2010-12-31'