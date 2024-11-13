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


# Given the data below, I need to create another CSV with the following columns: category, segment, speed, speed_min, speed_max

df = pd.read_csv('data/giro_rigo_average_speeds_segments.csv')

# Prepare a list to hold the transformed data
transformed_data = []

# Define the segments based on the column names
segments = ['Palmas', 'Km33', 'Raya', 'Km119', 'Final']

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    category = row['category']
    #print header names
    print(row.keys())

    for segment in segments:
        # Extract the average, min, and max speeds for each segment
        speed_avg = row[f'AVERAGE of avg_speed_split_{segment.lower()}']
        speed_min = row[f'MIN of avg_speed_split_{segment.lower()}']
        speed_max = row[f'MAX of avg_speed_split_{segment.lower()}']

        # Append the transformed row to the list
        transformed_data.append([category, segment, speed_avg, speed_min, speed_max])

# Create a new DataFrame from the transformed data
transformed_df = pd.DataFrame(transformed_data, columns=['category', 'segment', 'speed_avg', 'speed_min', 'speed_max'])

# each category should have a init value of 0 in all columns, new segment called "init"
for category in transformed_df['category'].unique():
    init_row = {'category': category, 'segment': 'Init', 'speed_avg': 0, 'speed_min': 0, 'speed_max': 0}
    transformed_df = pd.concat([transformed_df, pd.DataFrame([init_row])], ignore_index=True)

# Write the transformed DataFrame to a new CSV file
transformed_df.to_csv('data/giro_rigo_average_speeds_segments_transformed.csv', index=False)


# Given the data data/giro_de_rigo_times_with_positions_finishers.csv
# I want to create a column for each category and each row should bin the total time in 30 minutes intervals (between 4 hours and 10 hours)
# the value of each row and category should be the percentage of participants that fall into that bin for that category, each column should sum 100%
# Example:
# bin -> elite -> categoría a
# 4:00 - 4:30 -> 10% -> 10%
# 4:30 - 5:00 -> 20% -> 20%
# 5:00 - 5:30 -> 10% -> 10%
# ...
# 9:30 - 10:00 -> 1%

# Read the CSV file into a DataFrame
df = pd.read_csv('data/giro_de_rigo_times_with_positions_finishers.csv')

# Define the time bins (in seconds) each 15 minutes startint in 4 hours up to 8 hours)
bins = np.array([14400, 16200, 18000, 19800, 21600, 23400, 25200, 27000, 28800, 30600, 32400])

# Create a new DataFrame to store the binned data
binned_data = pd.DataFrame()

# Iterate over each category
categories = df['category'].unique()
for category in categories:
    # Filter the DataFrame for the current category
    category_df = df[df['category'] == category]

    #print(category_df.head())

    # Bin the total times
    binned_counts, _ = np.histogram(category_df['chip_time'], bins=bins)

    #print(f"Binned counts for category {category}: {binned_counts}")

    # Calculate the percentage for each bin
    binned_percentages = (binned_counts / binned_counts.sum()) * 100

    #print(f"Binned percentages for category {category}: {binned_percentages}")

    # Add the percentages to the binned_data DataFrame
    binned_data[category] = binned_percentages


# Create a column for the bin labels
bin_labels = [f"{int(bins[i]//3600)}:{int((bins[i]%3600)//60):02d} - {int(bins[i+1]//3600)}:{int((bins[i+1]%3600)//60):02d}" for i in range(len(bins)-1)]
binned_data['bin'] = bin_labels

# Reorder columns to have 'bin' as the first column
binned_data = binned_data[['bin'] + list(categories)]


# print dataframe
print(binned_data)

# Write the binned data to a new CSV file
binned_data.to_csv('data/binned_participant_percentages.csv', index=False)