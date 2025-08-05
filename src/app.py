from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np # pandas uses numpy, so it's good practice to import

# Initialize Flask App
app = Flask(__name__)
CORS(app)  # This enables Cross-Origin Resource Sharing

# --- Load and Prepare Data ---
prices_df = pd.read_csv(r'C:\Users\user\Documents\Datasience\birhan_energies_oil_analysis\data\01_processed\BrentOilPrices_Cleaned.csv')
events_df = pd.read_csv(r'C:\Users\user\Documents\Datasience\birhan_energies_oil_analysis\data\compiled\events.csv')

prices_df['Date'] = pd.to_datetime(prices_df['Date'], errors='coerce')
events_df['EventDate'] = pd.to_datetime(events_df['EventDate'], errors='coerce')

# Drop any rows where the date could not be parsed
prices_df.dropna(subset=['Date'], inplace=True)
events_df.dropna(subset=['EventDate'], inplace=True)

prices_df['Log_Return'] = (prices_df['Price'] / prices_df['Price'].shift(1)).apply(np.log)
prices_df = prices_df.sort_values('Date').reset_index(drop=True)

# Now, replace NaN in numerical columns with None for JSON. The 'Date' column is clean.
prices_df = prices_df.where(pd.notnull(prices_df), None)


# --- (Changepoint data remains the same) ---
changepoint_data = {
    'startDate': '2008-05-19',
    'endDate': '2008-08-21',
    'description': 'Volatility Transition Period (GFC Build-up)',
    'impact': { 'metric': 'Daily Volatility Increase', 'value': '57.89%' }
}

# --- CORRECTED API Endpoint for Price Data ---

@app.route('/api/price-data')
def get_price_data():
    """ Serves filtered price and log return data. """
    start_date_str = request.args.get('start')
    end_date_str = request.args.get('end')

    # Start with a copy. The 'Date' column is already datetime-compatible from startup.
    filtered_df = prices_df.copy()
    
    # The 'Date' column may contain None if loaded that way, so convert it back to datetime for filtering
    # but handle the None values gracefully.
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])

    if start_date_str:
        start_date = pd.to_datetime(start_date_str)
        filtered_df = filtered_df[filtered_df['Date'] >= start_date]
    
    if end_date_str:
        end_date = pd.to_datetime(end_date_str)
        filtered_df = filtered_df[filtered_df['Date'] <= end_date]
    
    # Prepare data for JSON, converting datetimes back to strings
    data_to_send = filtered_df.copy()
    data_to_send['Date'] = data_to_send['Date'].dt.strftime('%Y-%m-%d')
    
    return jsonify(data_to_send.to_dict(orient='records'))

# --- (Other endpoints remain the same) ---
@app.route('/api/events')
def get_events():
    data = events_df.copy()
    data['EventDate'] = data['EventDate'].dt.strftime('%Y-%m-%d')
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/changepoint')
def get_changepoint():
    return jsonify(changepoint_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)