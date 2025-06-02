import pandas as pd

df = pd.read_csv("data/ruta_medellin_2025/race_results_general_sorted.csv")

print(df.head())

# total participants
print(f"Total participants: {df['rank_general'].count()}")

print("-" * 100)

# print the distribution of categories and the number of runners in each category, add the percentage of the total participants. Sort by percentage descending
print("Number of participants per category:")
df_sorted = df.sort_values(by='rank_general', ascending=False)
for category in df_sorted['Category'].unique():
    print(f"{category}: {df_sorted[df_sorted['Category'] == category]['rank_general'].count()} ({df_sorted[df_sorted['Category'] == category]['rank_general'].count() / df_sorted['rank_general'].count() * 100:.2f}%)")

print("-" * 100)

# print the average time for each category, add the time in hh:mm:ss
print("Average time per category:")
for category in df['Category'].unique():
    print(f"{category}: {pd.to_datetime(df[df['Category'] == category]['Total Secs'].mean(), unit='s').strftime('%H:%M:%S')}")

print("-" * 100)

# Speeds (lowest, highest, average) per category, add the speed in km/h to 2 decimal places
print("Speeds (lowest, highest, average) per category:")
for category in df['Category'].unique():
    print(f"{category}: {df[df['Category'] == category]['Speed (km/h)'].min():.2f}, {df[df['Category'] == category]['Speed (km/h)'].max():.2f}, {df[df['Category'] == category]['Speed (km/h)'].mean():.2f}")

print("-" * 100)

# Segment analysis
print("Segment analysis:")
print("Segment 1 analysis per category. Percentiles 5th, 10th, 25th, 50th, 75th, 90th:")
# add percentiles 5th, 10th, 25th, 50th, 75th, 90th
for category in df['Category'].unique():
    quantile_5 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
    quantile_10 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
    quantile_25 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
    quantile_50 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
    quantile_75 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
    quantile_90 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')
    print(f"{category}: {quantile_5}, {quantile_10}, {quantile_25}, {quantile_50}, {quantile_75}, {quantile_90}")

print("-" * 100)

# Segment 2 analysis per category
print("Segment 2 analysis per category. Percentiles 5th, 10th, 25th, 50th, 75th, 90th:")
# add percentiles 5th, 10th, 25th, 50th, 75th, 90th
for category in df['Category'].unique():
    quantile_5 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
    quantile_10 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
    quantile_25 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
    quantile_50 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
    quantile_75 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
    quantile_90 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')
    print(f"{category}: {quantile_5}, {quantile_10}, {quantile_25}, {quantile_50}, {quantile_75}, {quantile_90}")

print("-" * 100)

# Segment 3 analysis per category
print("Segment 3 analysis per category. Percentiles 5th, 10th, 25th, 50th, 75th, 90th:")
# add percentiles 5th, 10th, 25th, 50th, 75th, 90th
for category in df['Category'].unique():
    quantile_5 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
    quantile_10 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
    quantile_25 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
    quantile_50 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
    quantile_75 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
    quantile_90 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')
    print(f"{category}: {quantile_5}, {quantile_10}, {quantile_25}, {quantile_50}, {quantile_75}, {quantile_90}")

print("-" * 100)

print("Total time analysis per category. Percentiles 5th, 10th, 25th, 50th, 75th, 90th:")
for category in df['Category'].unique():
    quantile_5 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
    quantile_10 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
    quantile_25 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
    quantile_50 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
    quantile_75 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
    quantile_90 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')
    print(f"{category}: {quantile_5}, {quantile_10}, {quantile_25}, {quantile_50}, {quantile_75}, {quantile_90}")

#percentiles of the total times without category
quantile_5 = pd.to_datetime(df['Total Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
quantile_10 = pd.to_datetime(df['Total Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
quantile_25 = pd.to_datetime(df['Total Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
quantile_50 = pd.to_datetime(df['Total Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
quantile_75 = pd.to_datetime(df['Total Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
quantile_90 = pd.to_datetime(df['Total Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')
print(f"Total time: {quantile_5}, {quantile_10}, {quantile_25}, {quantile_50}, {quantile_75}, {quantile_90}")