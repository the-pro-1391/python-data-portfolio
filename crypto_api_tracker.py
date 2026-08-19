import os
import json
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# 1. SET PANDAS DISPLAY OPTIONS
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x) 

def fetch_crypto_data(csv_filepath):
    """Fetches live cryptocurrency data from CoinMarketCap API and appends to a CSV."""
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
    parameters = {
      'start': '1', 
      'limit': '15', 
      'convert': 'USD' 
    }
    headers = {
      'Accepts': 'application/json', 
      # SECURITY UPGRADE: Removed the hardcoded key for GitHub
      'X-CMC_PRO_API_KEY': 'YOUR_API_KEY_HERE', 
    }

    session = Session() 
    session.headers.update(headers) 

    try:
        response = session.get(url, params=parameters, timeout=15) 
        data = json.loads(response.text) 
        
        df = pd.json_normalize(data['data']) 
        df['Timestamp'] = pd.Timestamp.now() 
        
        # Check if file exists to append or write new headers
        if not os.path.isfile(csv_filepath): 
            df.to_csv(csv_filepath, header=True, index=False) 
        else: 
            df.to_csv(csv_filepath, mode='a', header=False, index=False) 
            
        print("✅ SUCCESS: Data pulled and saved to CSV!")
            
    except (ConnectionError, Timeout, TooManyRedirects) as e: 
        print(f"⚠️ API BLOCKED/FAILED: {e}") 

if __name__ == "__main__":
    # Use a relative path for GitHub portability
    target_csv = 'crypto_api_data.csv'
    
    # 2. RUN THE AUTOMATION LOOP
    print("Starting API Loop...")
    for i in range(2): 
        fetch_crypto_data(target_csv) 
        time.sleep(5) 

    # 3. LOAD AND VISUALIZE DATA
    try:
        df_raw = pd.read_csv(target_csv) 
        print("Building charts...")

        # PREPARE TREND DATA (Renamed variables for readability)
        percent_cols = [
            'quote.USD.percent_change_1h', 'quote.USD.percent_change_24h',
            'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d',
            'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'
        ]
        
        df_grouped = df_raw.groupby('name', sort=False)[percent_cols].mean() 
        df_stacked = df_grouped.stack().to_frame(name='values').reset_index() 
        df_trends = df_stacked.rename(columns={'level_1': 'percent_change'}) 
        
        # Clean up the x-axis labels
        df_trends['percent_change'] = df_trends['percent_change'].replace(
            percent_cols, ['1h', '24h', '7d', '30d', '60d', '90d']
        )

        # VISUALIZATION 1: POINT PLOT
        sns.catplot(x='percent_change', y='values', hue='name', data=df_trends, kind='point', height=6, aspect=2) 
        plt.title("Cryptocurrency Percent Change Trends")
        plt.show() 

        # VISUALIZATION 2: BITCOIN LINE PLOT
        df_bitcoin = df_raw[['name', 'quote.USD.price', 'Timestamp']].query("name == 'Bitcoin'") 

        plt.figure(figsize=(10, 5))
        sns.set_theme(style="darkgrid") 
        sns.lineplot(x='Timestamp', y='quote.USD.price', data=df_bitcoin) 
        plt.title("Bitcoin Price Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show() 

    except FileNotFoundError:
        print("WARNING: Charts could not be built. Check your internet or API key.")