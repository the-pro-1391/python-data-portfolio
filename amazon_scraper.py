import requests
from bs4 import BeautifulSoup
import datetime
import csv
import os
import time
import pandas as pd
# import smtplib  # (Uncomment this later if you want to add email alerts for price drops)

def check_price():
    """Scrapes Amazon for a specific product's price and logs it to a CSV."""
    
    URL = 'https://www.amazon.in/Chitpatang-Feelings-T-Shirt-Developer-Streetwear/dp/B0H4H6B3S1/ref=sr_1_3'

    # Headers help bypass Amazon's basic bot detection
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
        "DNT": "1",
        "Connection": "close", 
        "Upgrade-Insecure-Requests": "1"
    }

    print("Fetching data from Amazon...")
    page = requests.get(URL, headers=headers)
    
    # We only need one BeautifulSoup object (prettify() slows down the script)
    soup = BeautifulSoup(page.content, "html.parser")

    # Use a relative path so the script works on any computer that downloads it
    csv_path = 'amazon_price_data.csv'

    try:
        # 1. Grab Title and Price safely
        title = soup.find(id='productTitle').get_text().strip()
        raw_price = soup.find("span", {"class": "a-price-whole"}).get_text().strip()
        
        # Clean the price (Amazon sometimes adds trailing dots or commas like '499.' or '1,499')
        clean_price = raw_price.replace(',', '').replace('.', '')
        
        # 2. Get today's date
        today = datetime.date.today()
        
        # 3. Check if the file exists BEFORE we open it, so we know if we need headers
        file_exists = os.path.isfile(csv_path)

        # 4. Append to the CSV
        with open(csv_path, 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            
            # If the file is brand new, write the column headers first
            if not file_exists:
                writer.writerow(['Title', 'Price', 'Date'])
                
            # Write the scraped data
            writer.writerow([title, clean_price, today])
            
        print(f"✅ SUCCESS: Logged '{title[:30]}...' at ₹{clean_price} on {today}")

    except AttributeError:
        print("⚠️ FAILED: Amazon sent a CAPTCHA or changed their HTML layout. No data saved.")

# --- SCRIPT EXECUTION ---

if __name__ == "__main__":
    # 1. Run the function once to test it
    check_price()

    # 2. Open the CSV with Pandas to prove it worked
    csv_path = 'amazon_price_data.csv'
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        print("\n--- Current Data Inside Your CSV ---")
        print(df.tail(5)) # Print just the last 5 rows to keep the terminal clean
    else:
        print("\nWARNING: CSV not found. The scrape likely failed.")

    # 3. The Automation Loop (Uncomment to run daily)
    # while True:
    #     check_price()
    #     time.sleep(86400) # 24 hours