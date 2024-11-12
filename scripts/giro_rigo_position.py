import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('data/giro_de_rigo_times.csv')

#count how many split final are less than 32536 (1:15:34) but any of the other splits are 0; then print a sample of 20 of them
print('Number of rows where split_final is less than 32536 and any of the other splits are 0: ', df[(df['split_final'] < 32536) & ((df['split_palmas'] == 0) | (df['split_raya'] == 0) | (df['split_km33'] == 0) | (df['split_km119'] == 0))].shape[0])

# Convert 'split_final' to float to handle 'inf' values
df['split_final'] = df['split_final'].astype(float)

# Replace the value of 'split_final' with float('inf') for specific conditions
df.loc[
    (df['split_final'] < 32536) &
    ((df['split_palmas'] == 0) |
     (df['split_raya'] == 0) |
     (df['split_km33'] == 0) |
     (df['split_km119'] == 0)),
    'split_final'
] = float('inf')

# Function to calculate general and category positions for a given split
def calculate_positions(df, split_column):
    # Convert the column to float to handle 'inf' values
    df[split_column] = df[split_column].astype(float)

    # Temporarily replace 0 values with a large number to ensure they rank last
    df[split_column] = df[split_column].replace(0, float('inf'))
    # replace the value of split final to float('inf') of rows that matches the following condition:
    df.loc[(df['split_final'] < 32536) & ((df['split_palmas'] == 0) | (df['split_raya'] == 0) | (df['split_km33'] == 0) | (df['split_km119'] == 0)), 'split_final'] = float('inf')

    # General position with unique ranks
    df[f'position_general_{split_column}'] = df[split_column].rank(method='first').astype(int)

    # Category position with unique ranks
    df[f'position_category_{split_column}'] = df.groupby('category')[split_column].rank(method='first').astype(int)

    # Replace inf values with None
    df[split_column] = df[split_column].replace(float('inf'), None)
    df[f'position_general_{split_column}'] = df[f'position_general_{split_column}'].replace(float('inf'), None)
    df[f'position_category_{split_column}'] = df[f'position_category_{split_column}'].replace(float('inf'), None)

def calculate_auxiliary_positions(df):
    # Count the number of non-null times for each row
    df['non_null_times'] = df[['split_palmas', 'split_km33', 'split_raya', 'split_km119', 'split_final']].notnull().sum(axis=1)

    # Create a mask for rows with all 5 times
    all_times_mask = df['non_null_times'] == 5

    # Initialize the auxiliary position column
    df['auxiliary_position_general_split_final'] = None

    # Assign the same value as position_general_split_final for rows with all 5 times
    df.loc[all_times_mask, 'auxiliary_position_general_split_final'] = df.loc[all_times_mask, 'position_general_split_final']

    # Rank the remaining rows based on the number of non-null times, in descending order
    # and then by position_general_split_final
    remaining_df = df.loc[~all_times_mask].copy()
    remaining_df.sort_values(by=['non_null_times', 'position_general_split_final'], ascending=[False, True], inplace=True)

    # Assign ranks, starting from the maximum rank of those with all times
    max_rank = df.loc[all_times_mask, 'position_general_split_final'].max() if not df.loc[all_times_mask].empty else 0
    remaining_df['auxiliary_position_general_split_final'] = range(max_rank + 1, max_rank + 1 + len(remaining_df))

    # Update the original DataFrame
    df.loc[~all_times_mask, 'auxiliary_position_general_split_final'] = remaining_df['auxiliary_position_general_split_final']

    # Drop the temporary column
    df.drop(columns='non_null_times', inplace=True)

#print max value of each split column with the text of the split, excluding inf values
print('split_palmas: ', df['split_palmas'].max())
print('split_raya: ', df['split_raya'].max())
print('split_km33: ', df['split_km33'].max())
print('split_km119: ', df['split_km119'].max())
print('split_final: ', df['split_final'].max())

# Calculate positions for each split
calculate_positions(df, 'split_palmas')
calculate_positions(df, 'split_km33')
calculate_positions(df, 'split_raya')
calculate_positions(df, 'split_km119')
calculate_positions(df, 'split_final')
calculate_auxiliary_positions(df)

# for each split we need to average speed in km/h Considering the following distances:
# split palmas: 15.75 km
# split km33: 33.0 km
# split raya: 6.31 km
# split km119: 119.0 km
# split final: 155.54 km
# Define the distances for each split
distances = {
    'split_palmas': 15.75,
    'split_km33': 33.0,
    'split_raya': 6.31,
    'split_km119': 119.0,
    'split_final': 155.54
}

# Calculate average speed in km/h for each split
for split, distance in distances.items():
  df[split] = df[split].astype(float)
  df[f'avg_speed_{split}'] = (distance / (df[split] / 3600)).round(3)

# sort df by the following columns: auxiliary_position_general_split_final, position_general_split_final ascending
df = df.sort_values(by=['auxiliary_position_general_split_final', 'position_general_split_final'], ascending=[True, True])

# drop the following columns: track, event, date, country, age, delay, penalty, team
df.drop(columns=['track', 'event', 'date', 'country', 'age', 'delay', 'penalty', 'team'], inplace=True)

# Save the updated DataFrame to a new CSV file
df.to_csv('data/giro_de_rigo_times_with_positions.csv', index=False)

# filter rows where all splits are not null
df = df[df[['split_palmas', 'split_km33', 'split_raya', 'split_km119', 'split_final']].notnull().all(axis=1)]

# count rows of df
print('Number of rows where all splits are not null: ', df.shape[0])

# save to csv
df.to_csv('data/giro_de_rigo_times_with_positions_finishers.csv', index=False)