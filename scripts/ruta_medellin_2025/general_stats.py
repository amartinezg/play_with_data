import pandas as pd

df = pd.read_csv("data/ruta_medellin_2025/race_results_general_sorted.csv")

print(df.head())

# total participants
total_participants_df = pd.DataFrame([{'Total Participants': df['rank_general'].count()}])
total_participants_df.to_csv("data/ruta_medellin_2025/total_participants.csv", index=False)
print("Saved total participants to data/ruta_medellin_2025/total_participants.csv")

print("-" * 100)

# Distribution of categories
df_sorted = df.sort_values(by='rank_general', ascending=False)
category_data = []
for category in df_sorted['Category'].unique():
    count = df_sorted[df_sorted['Category'] == category]['rank_general'].count()
    percentage = count / df_sorted['rank_general'].count() * 100
    category_data.append({'Category': category, 'Count': count, 'Percentage': percentage})
category_df = pd.DataFrame(category_data)
category_df.to_csv("data/ruta_medellin_2025/category_distribution.csv", index=False)
print("Saved category distribution to data/ruta_medellin_2025/category_distribution.csv")

print("-" * 100)

# Average time per category
avg_time_data = []
for category in df['Category'].unique():
    avg_time_seconds = df[df['Category'] == category]['Total Secs'].mean()
    avg_time_hms = pd.to_datetime(avg_time_seconds, unit='s').strftime('%H:%M:%S')
    avg_time_data.append({'Category': category, 'Average Time (s)': avg_time_seconds, 'Average Time (hh:mm:ss)': avg_time_hms})
avg_time_df = pd.DataFrame(avg_time_data)
avg_time_df.to_csv("data/ruta_medellin_2025/average_time_per_category.csv", index=False)
print("Saved average time per category to data/ruta_medellin_2025/average_time_per_category.csv")

print("-" * 100)

# Speeds (lowest, highest, average) per category
speeds_data = []
for category in df['Category'].unique():
    min_speed = df[df['Category'] == category]['Speed (km/h)'].min()
    max_speed = df[df['Category'] == category]['Speed (km/h)'].max()
    mean_speed = df[df['Category'] == category]['Speed (km/h)'].mean()
    speeds_data.append({
        'Category': category,
        'Min Speed (km/h)': min_speed,
        'Max Speed (km/h)': max_speed,
        'Mean Speed (km/h)': mean_speed
    })
speeds_df = pd.DataFrame(speeds_data)
speeds_df.to_csv("data/ruta_medellin_2025/speeds_per_category.csv", index=False)
print("Saved speeds per category to data/ruta_medellin_2025/speeds_per_category.csv")

print("-" * 100)

# Segment 1 analysis per category
segment1_data = []
for category in df['Category'].unique():
    quantile_5 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
    quantile_10 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
    quantile_25 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
    quantile_50 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
    quantile_75 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
    quantile_90 = pd.to_datetime(df[df['Category'] == category]['Segment 1 Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')
    segment1_data.append({
        'Category': category,
        '5th Percentile': quantile_5,
        '10th Percentile': quantile_10,
        '25th Percentile': quantile_25,
        '50th Percentile': quantile_50,
        '75th Percentile': quantile_75,
        '90th Percentile': quantile_90
    })
segment1_df = pd.DataFrame(segment1_data)
segment1_df.to_csv("data/ruta_medellin_2025/segment1_analysis_per_category.csv", index=False)
print("Saved Segment 1 analysis per category to data/ruta_medellin_2025/segment1_analysis_per_category.csv")

print("-" * 100)

# Segment 2 analysis per category
segment2_data = []
for category in df['Category'].unique():
    quantile_5 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
    quantile_10 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
    quantile_25 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
    quantile_50 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
    quantile_75 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
    quantile_90 = pd.to_datetime(df[df['Category'] == category]['Segment 2 Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')
    segment2_data.append({
        'Category': category,
        '5th Percentile': quantile_5,
        '10th Percentile': quantile_10,
        '25th Percentile': quantile_25,
        '50th Percentile': quantile_50,
        '75th Percentile': quantile_75,
        '90th Percentile': quantile_90
    })
segment2_df = pd.DataFrame(segment2_data)
segment2_df.to_csv("data/ruta_medellin_2025/segment2_analysis_per_category.csv", index=False)
print("Saved Segment 2 analysis per category to data/ruta_medellin_2025/segment2_analysis_per_category.csv")

print("-" * 100)

# Segment 3 analysis per category
segment3_data = []
for category in df['Category'].unique():
    quantile_5 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
    quantile_10 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
    quantile_25 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
    quantile_50 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
    quantile_75 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
    quantile_90 = pd.to_datetime(df[df['Category'] == category]['Segment 3 Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')
    segment3_data.append({
        'Category': category,
        '5th Percentile': quantile_5,
        '10th Percentile': quantile_10,
        '25th Percentile': quantile_25,
        '50th Percentile': quantile_50,
        '75th Percentile': quantile_75,
        '90th Percentile': quantile_90
    })
segment3_df = pd.DataFrame(segment3_data)
segment3_df.to_csv("data/ruta_medellin_2025/segment3_analysis_per_category.csv", index=False)
print("Saved Segment 3 analysis per category to data/ruta_medellin_2025/segment3_analysis_per_category.csv")

print("-" * 100)

# Total time analysis per category
total_time_data_cat = []
for category in df['Category'].unique():
    quantile_5 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
    quantile_10 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
    quantile_25 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
    quantile_50 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
    quantile_75 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
    quantile_90 = pd.to_datetime(df[df['Category'] == category]['Total Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')
    total_time_data_cat.append({
        'Category': category,
        '5th Percentile': quantile_5,
        '10th Percentile': quantile_10,
        '25th Percentile': quantile_25,
        '50th Percentile': quantile_50,
        '75th Percentile': quantile_75,
        '90th Percentile': quantile_90
    })
total_time_cat_df = pd.DataFrame(total_time_data_cat)
total_time_cat_df.to_csv("data/ruta_medellin_2025/total_time_analysis_per_category.csv", index=False)
print("Saved Total time analysis per category to data/ruta_medellin_2025/total_time_analysis_per_category.csv")

print("-" * 100)

# Percentiles of the total times without category
quantile_5_overall = pd.to_datetime(df['Total Secs'].quantile(0.05), unit='s').strftime('%H:%M:%S')
quantile_10_overall = pd.to_datetime(df['Total Secs'].quantile(0.1), unit='s').strftime('%H:%M:%S')
quantile_25_overall = pd.to_datetime(df['Total Secs'].quantile(0.25), unit='s').strftime('%H:%M:%S')
quantile_50_overall = pd.to_datetime(df['Total Secs'].quantile(0.5), unit='s').strftime('%H:%M:%S')
quantile_75_overall = pd.to_datetime(df['Total Secs'].quantile(0.75), unit='s').strftime('%H:%M:%S')
quantile_90_overall = pd.to_datetime(df['Total Secs'].quantile(0.9), unit='s').strftime('%H:%M:%S')

overall_percentiles_data = [{
    'Percentile': '5th', 'Time': quantile_5_overall
}, {
    'Percentile': '10th', 'Time': quantile_10_overall
}, {
    'Percentile': '25th', 'Time': quantile_25_overall
}, {
    'Percentile': '50th', 'Time': quantile_50_overall
}, {
    'Percentile': '75th', 'Time': quantile_75_overall
}, {
    'Percentile': '90th', 'Time': quantile_90_overall
}]
overall_percentiles_df = pd.DataFrame(overall_percentiles_data)
overall_percentiles_df.to_csv("data/ruta_medellin_2025/overall_total_time_percentiles.csv", index=False)
print("Saved overall total time percentiles to data/ruta_medellin_2025/overall_total_time_percentiles.csv")