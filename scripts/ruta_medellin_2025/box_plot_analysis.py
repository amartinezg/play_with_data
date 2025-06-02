import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os
import numpy as np

def format_seconds_to_hhmmss(seconds, pos=None):
    """Converts seconds (float) to HH:MM:SS string format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def create_total_time_by_category_boxplot():
    """
    Loads the race results data and creates a box plot of total race times
    (Total Secs) grouped by category, with y-axis in HH:MM:SS format.
    """
    # Step 1: Define the path to the data file
    script_dir = os.path.dirname(__file__)
    data_file_path = os.path.join(script_dir, '..', '..', 'data', 'ruta_medellin_2025', 'race_results_general_sorted.csv')

    # Step 2: Load the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(data_file_path)
    except FileNotFoundError:
        print(f"Error: The file {data_file_path} was not found.")
        print("Please ensure the path is correct and the file exists.")
        return
    except Exception as e:
        print(f"Error loading the CSV file: {e}")
        return

    # Step 3: Data Check/Preparation
    if not pd.api.types.is_numeric_dtype(df['Total Secs']):
        print("Warning: 'Total Secs' column is not numeric. Attempting conversion...")
        try:
            df['Total Secs'] = pd.to_numeric(df['Total Secs'])
        except ValueError:
            print("Error: Could not convert 'Total Secs' to a numeric type.")
            print("Please check the column for non-numeric values or incorrect decimal separators.")
            return

    if 'Category' not in df.columns:
        print("Error: 'Category' column not found in the DataFrame.")
        return

    min_time_data = df['Total Secs'].min()
    max_time_data = df['Total Secs'].max()

    # Step 4: Create the Box Plot
    plt.figure(figsize=(6, 6))

    ax = sns.boxplot(x='Category', y='Total Secs', hue='Category', data=df, palette='viridis', legend=False)

    # Step 5: Enhance the Plot & Format Y-axis
    plt.title('Distribución de tiempos totales', fontsize=16)
    plt.xlabel('Categoría', fontsize=14)
    plt.ylabel('Tiempo total (HH:MM:SS)', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    formatter = mticker.FuncFormatter(format_seconds_to_hhmmss)
    ax.yaxis.set_major_formatter(formatter)

    # Set y-axis ticks for more granularity (e.g., every 10 minutes = 600 seconds)
    tick_interval = 600
    current_y_lim = ax.get_ylim()
    start_tick = np.floor(current_y_lim[0] / tick_interval) * tick_interval
    end_tick = np.ceil(current_y_lim[1] / tick_interval) * tick_interval

    if start_tick > min_time_data - tick_interval:
        start_tick = np.floor((min_time_data - (tick_interval/2)) / tick_interval) * tick_interval
        if start_tick < 0: start_tick = 0

    y_ticks = np.arange(start_tick, end_tick + tick_interval, tick_interval)
    ax.set_yticks(y_ticks)
    ax.set_ylim(y_ticks[0] - (tick_interval * 0.1), y_ticks[-1] + (tick_interval * 0.1))

    plt.tight_layout()

    # Step 6: Save and Show the plot
    script_dir = os.path.dirname(__file__)
    plot_save_dir = os.path.join(script_dir, '..', '..', 'data', 'ruta_medellin_2025', 'images')
    os.makedirs(plot_save_dir, exist_ok=True)
    plot_save_path = os.path.join(plot_save_dir, 'total_time_by_category_boxplot.png')

    plt.savefig(plot_save_path, dpi=100)
    print(f"Plot saved to {plot_save_path}")

    plt.show()

if __name__ == '__main__':
    create_total_time_by_category_boxplot()
