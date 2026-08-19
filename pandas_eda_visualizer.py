import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_visualizations(file_path):
    """Reads a dataset and automatically generates and saves EDA visualizations."""
    
    print("Loading data and setting up charts...")
    
    # 1. Safely load the data
    try:
        df = pd.read_csv(file_path)
        df = df.set_index('Date')
    except FileNotFoundError:
        print(f"⚠️ Error: Could not find {file_path}. Please check the folder.")
        return

    # 2. Set the professional style
    plt.style.use('fivethirtyeight')

    # 3. Create an output folder for the images
    output_folder = 'eda_exports'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"📁 Created folder: {output_folder}/")

    # --- VISUALIZATION 1: Line Trend ---
    # Using a figure size ensures the chart isn't cramped
    plt.figure(figsize=(10, 5))
    df.plot(kind='line', title='Ice Cream Ratings Over Time', xlabel='Date', ylabel='Scores', figsize=(10, 5))
    plt.tight_layout() # Prevents text from being cut off
    plt.savefig(f'{output_folder}/1_rating_trends.png')
    plt.close() # Closes the plot so the next one starts fresh

    # --- VISUALIZATION 2: Area Plot ---
    plt.figure(figsize=(10, 5))
    df.plot.area(title='Cumulative Rating Area', figsize=(10, 5), alpha=0.5)
    plt.tight_layout()
    plt.savefig(f'{output_folder}/2_area_distribution.png')
    plt.close()

    # --- VISUALIZATION 3: Scatter Plot ---
    plt.figure(figsize=(8, 6))
    df.plot.scatter(x='Texture Rating', y='Overall Rating', s=100, c='black', title='Texture vs. Overall Rating')
    plt.tight_layout()
    plt.savefig(f'{output_folder}/3_texture_scatter.png')
    plt.close()

    # --- VISUALIZATION 4: Histogram ---
    plt.figure(figsize=(8, 5))
    df.plot.hist(bins=10, alpha=0.7, title='Frequency of Ratings')
    plt.tight_layout()
    plt.savefig(f'{output_folder}/4_rating_histogram.png')
    plt.close()

    print(f"✅ SUCCESS: All visualizations saved to the '{output_folder}' folder!")

if __name__ == "__main__":
    # Use a relative path so it works when downloaded from GitHub
    csv_file = 'Ice Cream Ratings.csv'
    generate_visualizations(csv_file)