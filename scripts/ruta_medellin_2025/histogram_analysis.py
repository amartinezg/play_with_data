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

def create_histograms_by_category():
    """
    Loads race results and creates a grid of histograms for Total Secs by Category.
    """
    script_dir = os.path.dirname(__file__)
    data_file_path = os.path.join(script_dir, '..', '..', 'data', 'ruta_medellin_2025', 'race_results_general_sorted.csv')
    plot_save_dir = os.path.join(script_dir, '..', '..', 'data', 'ruta_medellin_2025', 'images')
    os.makedirs(plot_save_dir, exist_ok=True)
    plot_save_path = os.path.join(plot_save_dir, 'histograms_total_time_by_category.png')

    try:
        df = pd.read_csv(data_file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {data_file_path}")
        return
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    if 'Total Secs' not in df.columns or 'Category' not in df.columns:
        print("Error: Required columns 'Total Secs' or 'Category' not found.")
        return
    if not pd.api.types.is_numeric_dtype(df['Total Secs']):
        try:
            df['Total Secs'] = pd.to_numeric(df['Total Secs'])
        except ValueError:
            print("Error: 'Total Secs' could not be converted to numeric.")
            return

    categories = df['Category'].unique()
    n_categories = len(categories)

    n_cols = 3
    n_rows = int(np.ceil(n_categories / n_cols))

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 3.5 * n_rows), sharex=False)
    axes = axes.flatten()

    for i, category in enumerate(categories):
        ax = axes[i]
        category_df = df[df['Category'] == category]

        sns.histplot(data=category_df, x='Total Secs', ax=ax, kde=True, bins=15)

        ax.set_title(category, fontsize=10)
        ax.set_xlabel('Tiempo Total (HH:MM:SS)', fontsize=8)
        ax.set_ylabel('Participantes', fontsize=8)

        ax.xaxis.set_major_formatter(mticker.FuncFormatter(format_seconds_to_hhmmss))

        plt.setp(ax.get_xticklabels(), rotation=30, ha="right", fontsize=7)
        ax.tick_params(axis='y', labelsize=7)
        ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True, nbins=5))

    for j in range(i + 1, n_rows * n_cols):
        axes[j].set_visible(False)

    fig.suptitle('Distribución de Tiempos Totales por Categoría (Histogramas)', fontsize=16, y=1.02)
    plt.tight_layout(rect=[0, 0, 1, 0.98])

    try:
        plt.savefig(plot_save_path, dpi=100)
        print(f"Plot saved to {plot_save_path}")
    except Exception as e:
        print(f"Error saving plot: {e}")

    plt.show()

if __name__ == '__main__':
    create_histograms_by_category()
