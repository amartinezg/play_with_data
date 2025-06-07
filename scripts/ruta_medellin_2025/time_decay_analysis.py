import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os
import numpy as np

def plot_time_decay_analysis():
    """
    Loads sorted race results, creates a line chart of total time vs. rank,
    and highlights time percentiles.
    The resulting plot is saved as an image.
    """
    script_dir = os.path.dirname(__file__)
    data_file_path = os.path.join(script_dir, '..', '..', 'data', 'ruta_medellin_2025', 'race_results_general_sorted.csv')
    plot_save_dir = os.path.join(script_dir, '..', '..', 'data', 'ruta_medellin_2025', 'images')
    os.makedirs(plot_save_dir, exist_ok=True)
    plot_save_path = os.path.join(plot_save_dir, 'time_decay_analysis.png')

    try:
        df = pd.read_csv(data_file_path)
    except FileNotFoundError:
        print(f"Error: Data file not found at {data_file_path}")
        return
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    # Ensure required columns exist
    required_cols = ['rank_general', 'Total Secs']
    if not all(col in df.columns for col in required_cols):
        print(f"Error: Missing one or more required columns: {required_cols}")
        return

    # --- Plotting ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax1 = plt.subplots(1, 1, figsize=(15, 8))

    # --- Plot: Rank vs. Total Time ---
    ax1.plot(df['Total Secs'], df['rank_general'], color='royalblue')

    # Invert Y-axis so Rank 1 is at the top
    ax1.invert_yaxis()
    ax1.set_title('Decaimiento del Tiempo Total vs. Ranking General', fontsize=18)
    ax1.set_ylabel('Ranking General', fontsize=12)
    ax1.set_xlabel('Tiempo Total (HH:MM:SS)', fontsize=12)

    # Highlight percentiles
    percentiles = {
        'P10': df['Total Secs'].quantile(0.10),
        'P25': df['Total Secs'].quantile(0.25),
        'P50': df['Total Secs'].quantile(0.50),
        'P75': df['Total Secs'].quantile(0.75),
        'P90': df['Total Secs'].quantile(0.90),
    }
    colors = {'P10': 'cyan', 'P25': 'green', 'P50': 'orange', 'P75': 'red', 'P90': 'purple'}

    for p_name, p_value in percentiles.items():
        ax1.axvline(x=p_value, color=colors[p_name], linestyle='--', lw=1.5, label=f'{p_name} ({pd.to_datetime(p_value, unit="s").strftime("%H:%M:%S")})')

    ax1.legend(title='Percentiles de Tiempo')

    # Format X-axis to HH:MM:SS
    formatter = mticker.FuncFormatter(lambda s, x: pd.to_datetime(s, unit='s').strftime('%H:%M:%S'))
    ax1.xaxis.set_major_formatter(formatter)

    # Set x-axis major ticks every 15 minutes (900 seconds)
    ax1.xaxis.set_major_locator(mticker.MultipleLocator(900))
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

    # Set y-axis major ticks every 250 ranks
    ax1.yaxis.set_major_locator(mticker.MultipleLocator(250))

    # --- Final Layout and Save ---
    plt.tight_layout()

    try:
        plt.savefig(plot_save_path)
        print(f"Plot saved to {plot_save_path}")
    except Exception as e:
        print(f"Error saving plot: {e}")

    # plt.show() # Uncomment to display plot locally

if __name__ == '__main__':
    plot_time_decay_analysis()