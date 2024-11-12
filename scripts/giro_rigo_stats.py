import pandas as pd
import numpy as np
from scipy.stats import percentileofscore

# Read the CSV file
df = pd.read_csv('data/giro_de_rigo_times_with_positions_finishers.csv')

print("\n=== General Statistics ===")
print(f"Total participants: {len(df)}")
print(f"Total finishers: {len(df[df['split_final'] > 0])}")
print(f"DNF rate: {(1 - len(df[df['split_final'] > 0])/len(df))*100:.1f}%")

print("\n=== Category Distribution ===")
category_counts = df['category'].value_counts()
print(category_counts)

print("\n=== Time Statistics (HH:MM:SS) ===")
for split in ['split_palmas', 'split_km33', 'split_raya', 'split_km119', 'split_final']:
    # Filter out zeros and inf values in one line
    valid_times = df[(df[split] > 0) & (~np.isinf(df[split]))][split]

    if len(valid_times) > 0:
        print(f"\n{split}:")
        print(f"Fastest: {pd.to_datetime(valid_times.min(), unit='s').strftime('%H:%M:%S')}")
        print(f"Average: {pd.to_datetime(valid_times.mean(), unit='s').strftime('%H:%M:%S')}")
        print(f"Slowest: {pd.to_datetime(valid_times.max(), unit='s').strftime('%H:%M:%S')}")

print("\n=== Average Speeds (km/h) ===")
speed_columns = [col for col in df.columns if col.startswith('avg_speed_')]
for col in speed_columns:
    valid_speeds = df[(df[col] > 0) & (~np.isinf(df[col]))][col]
    if len(valid_speeds) > 0:
        print(f"\n{col}:")
        print(f"Fastest: {valid_speeds.max():.2f}")
        print(f"Average: {valid_speeds.mean():.2f}")
        print(f"Slowest: {valid_speeds.min():.2f}")

valid_palmas = df[(df['split_palmas'] > 0) & (~np.isinf(df['split_palmas']))]['split_palmas']
valid_km33 = df[(df['split_km33'] > 0) & (~np.isinf(df['split_km33']))]['split_km33']
valid_raya = df[(df['split_raya'] > 0) & (~np.isinf(df['split_raya']))]['split_raya']
valid_km119 = df[(df['split_km119'] > 0) & (~np.isinf(df['split_km119']))]['split_km119']
valid_final = df[(df['split_final'] > 0) & (~np.isinf(df['split_final']))]['split_final']

print("\n=== Percentiles Palmas ===")
print("5th percentile, ", pd.to_datetime(valid_palmas.quantile(0.05), unit='s').strftime('%H:%M:%S'), " - ", valid_palmas.quantile(0.05))
print("10th percentile: ", pd.to_datetime(valid_palmas.quantile(0.1), unit='s').strftime('%H:%M:%S'), " - ", valid_palmas.quantile(0.1))
print("25th percentile: ", pd.to_datetime(valid_palmas.quantile(0.25), unit='s').strftime('%H:%M:%S'), " - ", valid_palmas.quantile(0.25))
print("50th percentile: ", pd.to_datetime(valid_palmas.quantile(0.5), unit='s').strftime('%H:%M:%S'), " - ", valid_palmas.quantile(0.5))
print("75th percentile: ", pd.to_datetime(valid_palmas.quantile(0.75), unit='s').strftime('%H:%M:%S'), " - ", valid_palmas.quantile(0.75))
print("90th percentile: ", pd.to_datetime(valid_palmas.quantile(0.9), unit='s').strftime('%H:%M:%S'), " - ", valid_palmas.quantile(0.9))

# do the same math for each category
print(f"\n=== Percentiles Palmas for each category ===")
for category in df['category'].unique():
    valid_palmas_category = df[(df['category'] == category) & (df['split_palmas'] > 0) & (~np.isinf(df['split_palmas']))]['split_palmas']
    print(f"Palmas, {valid_palmas_category.quantile(0.05)}, {pd.to_datetime(valid_palmas_category.quantile(0.05), unit='s').strftime('%H:%M:%S')}, {valid_palmas_category.quantile(0.9)}, {pd.to_datetime(valid_palmas_category.quantile(0.9), unit='s').strftime('%H:%M:%S')}, {category}")
    #print("5th percentile, ", pd.to_datetime(valid_palmas_category.quantile(0.05), unit='s').strftime('%H:%M:%S'), ", ", valid_palmas_category.quantile(0.05))
    #print("10th percentile, ", pd.to_datetime(valid_palmas_category.quantile(0.1), unit='s').strftime('%H:%M:%S'), ", ", valid_palmas_category.quantile(0.1))
    #print("25th percentile, ", pd.to_datetime(valid_palmas_category.quantile(0.25), unit='s').strftime('%H:%M:%S'), ", ", valid_palmas_category.quantile(0.25))
    #print("50th percentile, ", pd.to_datetime(valid_palmas_category.quantile(0.5), unit='s').strftime('%H:%M:%S'), ", ", valid_palmas_category.quantile(0.5))
    #print("75th percentile, ", pd.to_datetime(valid_palmas_category.quantile(0.75), unit='s').strftime('%H:%M:%S'), ", ", valid_palmas_category.quantile(0.75))
    #print("90th percentile, ", pd.to_datetime(valid_palmas_category.quantile(0.9), unit='s').strftime('%H:%M:%S'), ", ", valid_palmas_category.quantile(0.9))

print(f"\n=== Percentiles KM33 for each category ===")
for category in df['category'].unique():
    valid_km33_category = df[(df['category'] == category) & (df['split_km33'] > 0) & (~np.isinf(df['split_km33']))]['split_km33']
    print(f"KM33, {valid_km33_category.quantile(0.05)}, {pd.to_datetime(valid_km33_category.quantile(0.05), unit='s').strftime('%H:%M:%S')}, {valid_km33_category.quantile(0.9)}, {pd.to_datetime(valid_km33_category.quantile(0.9), unit='s').strftime('%H:%M:%S')}, {category}")


print(f"\n=== Percentiles Raya for each category ===")
for category in df['category'].unique():
    valid_raya_category = df[(df['category'] == category) & (df['split_raya'] > 0) & (~np.isinf(df['split_raya']))]['split_raya']
    print(f"Raya, {valid_raya_category.quantile(0.05)}, {pd.to_datetime(valid_raya_category.quantile(0.05), unit='s').strftime('%H:%M:%S')}, {valid_raya_category.quantile(0.9)}, {pd.to_datetime(valid_raya_category.quantile(0.9), unit='s').strftime('%H:%M:%S')}, {category}")

print(f"\n=== Percentiles KM119 for each category ===")
for category in df['category'].unique():
    valid_km119_category = df[(df['category'] == category) & (df['split_km119'] > 0) & (~np.isinf(df['split_km119']))]['split_km119']
    print(f"KM119, {valid_km119_category.quantile(0.05)}, {pd.to_datetime(valid_km119_category.quantile(0.05), unit='s').strftime('%H:%M:%S')}, {valid_km119_category.quantile(0.9)}, {pd.to_datetime(valid_km119_category.quantile(0.9), unit='s').strftime('%H:%M:%S')}, {category}")

print(f"\n=== Percentiles Final for each category ===")
for category in df['category'].unique():
    valid_final_category = df[(df['category'] == category) & (df['split_final'] > 0) & (~np.isinf(df['split_final']))]['split_final']
    print(f"Final, {valid_final_category.quantile(0.05)}, {pd.to_datetime(valid_final_category.quantile(0.05), unit='s').strftime('%H:%M:%S')}, {valid_final_category.quantile(0.9)}, {pd.to_datetime(valid_final_category.quantile(0.9), unit='s').strftime('%H:%M:%S')}, {category}")

print("\n=== Percentiles KM33 ===")
print("5th percentile: ", pd.to_datetime(valid_km33.quantile(0.05), unit='s').strftime('%H:%M:%S'), " - ", valid_km33.quantile(0.05))
print("10th percentile: ", pd.to_datetime(valid_km33.quantile(0.1), unit='s').strftime('%H:%M:%S'), " - ", valid_km33.quantile(0.1))
print("25th percentile: ", pd.to_datetime(valid_km33.quantile(0.25), unit='s').strftime('%H:%M:%S'), " - ", valid_km33.quantile(0.25))
print("50th percentile: ", pd.to_datetime(valid_km33.quantile(0.5), unit='s').strftime('%H:%M:%S'), " - ", valid_km33.quantile(0.5))
print("75th percentile: ", pd.to_datetime(valid_km33.quantile(0.75), unit='s').strftime('%H:%M:%S'), " - ", valid_km33.quantile(0.75))
print("90th percentile: ", pd.to_datetime(valid_km33.quantile(0.9), unit='s').strftime('%H:%M:%S'), " - ", valid_km33.quantile(0.9))

print("\n=== Percentiles Raya ===")
print("5th percentile: ", pd.to_datetime(valid_raya.quantile(0.05), unit='s').strftime('%H:%M:%S'), " - ", valid_raya.quantile(0.05))
print("10th percentile: ", pd.to_datetime(valid_raya.quantile(0.1), unit='s').strftime('%H:%M:%S'), " - ", valid_raya.quantile(0.1))
print("25th percentile: ", pd.to_datetime(valid_raya.quantile(0.25), unit='s').strftime('%H:%M:%S'), " - ", valid_raya.quantile(0.25))
print("50th percentile: ", pd.to_datetime(valid_raya.quantile(0.5), unit='s').strftime('%H:%M:%S'), " - ", valid_raya.quantile(0.5))
print("75th percentile: ", pd.to_datetime(valid_raya.quantile(0.75), unit='s').strftime('%H:%M:%S'), " - ", valid_raya.quantile(0.75))
print("90th percentile: ", pd.to_datetime(valid_raya.quantile(0.9), unit='s').strftime('%H:%M:%S'), " - ", valid_raya.quantile(0.9))

print("\n=== Percentiles KM119 ===")
print("5th percentile: ", pd.to_datetime(valid_km119.quantile(0.05), unit='s').strftime('%H:%M:%S'), " - ", valid_km119.quantile(0.05))
print("10th percentile: ", pd.to_datetime(valid_km119.quantile(0.1), unit='s').strftime('%H:%M:%S'), " - ", valid_km119.quantile(0.1))
print("25th percentile: ", pd.to_datetime(valid_km119.quantile(0.25), unit='s').strftime('%H:%M:%S'), " - ", valid_km119.quantile(0.25))
print("50th percentile: ", pd.to_datetime(valid_km119.quantile(0.5), unit='s').strftime('%H:%M:%S'), " - ", valid_km119.quantile(0.5))
print("75th percentile: ", pd.to_datetime(valid_km119.quantile(0.75), unit='s').strftime('%H:%M:%S'), " - ", valid_km119.quantile(0.75))
print("90th percentile: ", pd.to_datetime(valid_km119.quantile(0.9), unit='s').strftime('%H:%M:%S'), " - ", valid_km119.quantile(0.9))

print("\n=== Percentiles Final ===")
print("5th percentile: ", pd.to_datetime(valid_final.quantile(0.05), unit='s').strftime('%H:%M:%S'), " - ", valid_final.quantile(0.05))
print("10th percentile: ", pd.to_datetime(valid_final.quantile(0.1), unit='s').strftime('%H:%M:%S'), " - ", valid_final.quantile(0.1))
print("25th percentile: ", pd.to_datetime(valid_final.quantile(0.25), unit='s').strftime('%H:%M:%S'), " - ", valid_final.quantile(0.25))
print("50th percentile: ", pd.to_datetime(valid_final.quantile(0.5), unit='s').strftime('%H:%M:%S'), " - ", valid_final.quantile(0.5))
print("75th percentile: ", pd.to_datetime(valid_final.quantile(0.75), unit='s').strftime('%H:%M:%S'), " - ", valid_final.quantile(0.75))
print("90th percentile: ", pd.to_datetime(valid_final.quantile(0.9), unit='s').strftime('%H:%M:%S'), " - ", valid_final.quantile(0.9))

# Calculate the percentile rank for the row with id 3677592
row_3677592 = df.loc[df['id'] == 3677592]
print(f"\n=== Percentiles for id {row_3677592['id'].values[0]} with name {row_3677592['name'].values[0]} ===")

percentile_palmas = percentileofscore(valid_palmas, row_3677592['split_palmas'].values[0])
percentile_km33 = percentileofscore(valid_km33, row_3677592['split_km33'].values[0])
percentile_raya = percentileofscore(valid_raya, row_3677592['split_raya'].values[0])
percentile_km119 = percentileofscore(valid_km119, row_3677592['split_km119'].values[0])
percentile_final = percentileofscore(valid_final, row_3677592['split_final'].values[0])

print(f"Palmas: {round(percentile_palmas, 2)}%. Pos: {row_3677592['position_general_split_palmas'].values[0]}")
print(f"KM33: {round(percentile_km33, 2)}%. Gained/Loss vs Palmas: {row_3677592['position_general_split_km33'].values[0] - row_3677592['position_general_split_palmas'].values[0]}")
print(f"Raya: {round(percentile_raya, 2)}%. Pos: {row_3677592['position_general_split_raya'].values[0]}")
print(f"KM119: {round(percentile_km119, 2)}%. Gained/Loss vs km 33: {row_3677592['position_general_split_km119'].values[0] - row_3677592['position_general_split_km33'].values[0]}")
print(f"Final: {round(percentile_final, 2)}%. Gained/Loss vs km 119: {row_3677592['position_general_split_final'].values[0] - row_3677592['position_general_split_km119'].values[0]}")

print(row_3677592.transpose())

def count_valid_times_with_percentages(df):
    # Define the split columns
    split_columns = ['split_palmas', 'split_km33', 'split_raya', 'split_km119', 'split_final']

    # Initialize a list to store the results
    results = []

    # Count for the general category
    general_counts = {'Category': 'General', 'Starting': len(df), 'Starting_%': 100}
    for split in split_columns:
        count = df[split].notnull().sum()
        general_counts[split] = count
        general_counts[f'{split}_%'] = (count / general_counts['Starting']) * 100
    results.append(general_counts)

    # Count for each distinct category
    for category in df['category'].unique():
        category_df = df[df['category'] == category]
        category_counts = {'Category': category, 'Starting': len(category_df), 'Starting_%': 100}
        for split in split_columns:
            count = category_df[split].notnull().sum()
            category_counts[split] = count
            category_counts[f'{split}_%'] = (count / category_counts['Starting']) * 100
        results.append(category_counts)

    # Convert the results to a DataFrame
    count_df = pd.DataFrame(results)

    # Print the DataFrame only columns with percentages
    print(count_df)

    # Save the DataFrame to a CSV file
    count_df.to_csv('data/split_counts_with_percentages_and_values.csv', index=False)

count_valid_times_with_percentages(df)

# how many rows did not start the race? count all rows where all splits are 0 or empty
not_started_count = df[df[['split_palmas', 'split_km33', 'split_raya', 'split_km119', 'split_final']].isnull().all(axis=1)].shape[0]
print(f"Number of participants who did not start the race: {not_started_count}")