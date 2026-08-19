# Python Data Portfolio 🐍

Welcome to my Python data and automation portfolio! This repository contains a collection of Python scripts demonstrating my ability to build automated ETL pipelines, extract unstructured data from the web, manage local file systems, and perform exploratory data analysis.

## 🛠️ Tech Stack & Libraries
* **Language:** Python 3
* **Data Manipulation & Visualization:** `pandas`, `seaborn`, and `matplotlib`
* **Web Scraping & APIs:** `requests`, `BeautifulSoup` (bs4), and `json`
* **Built-in Modules:** `os`, `shutil`, `csv`, and `time`

---

## 📂 Featured Projects

### 1. Cryptocurrency API ETL Pipeline
**File:** `crypto_api_tracker.py`
* **Objective:** Built an automated ETL pipeline that extracts live cryptocurrency pricing from the CoinMarketCap API.
* **Process:** Parsed complex JSON responses, normalized the data into a Pandas DataFrame, and automated continuous CSV logging. 
* **Insights:** Reshaped time-series data using `.groupby()` and `.stack()` to generate point-trend charts and Bitcoin price volatility plots using Seaborn and Matplotlib.

### 2. Amazon E-Commerce Web Scraper
**File:** `amazon_scraper.py`
* **Objective:** Developed an automated scraper to track product price fluctuations on Amazon over time.
* **Process:** Utilized custom HTTP headers to navigate basic bot protections and parsed the HTML DOM using BeautifulSoup to extract product titles and pricing data.
* **Insights:** Engineered automated data cleaning to format currency strings into integers and appended the daily records to a structured CSV dataset.

### 3. Local OS File Sorter
**File:** `local_file_automation.py`
* **Objective:** Created a system utility script to automatically organize cluttered directories.
* **Process:** Utilized the `os` and `shutil` libraries to traverse directories, dynamically map file extensions to specific target folders via dictionaries, and securely relocate files.

### 4. Pandas Exploratory Data Analysis (EDA)
**File:** `pandas_eda_visualizer.py`
* **Objective:** Developed an automated reporting script that reads tabular data and generates customized static visualizations.
* **Process:** Utilized `pandas` for data manipulation, index setting, and statistical structuring, alongside `matplotlib` to apply standardized styling.
* **Insights:** Engineered the script to automatically manage memory and export a suite of high-resolution `.png` files, including time-series lines, scatter distributions, and histograms, directly to a designated local directory.
