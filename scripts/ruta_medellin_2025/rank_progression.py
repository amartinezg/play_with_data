# read the race_results_general_sorted.csv file
# calculate the rank of each rider on each segment and add it to the dataframe
# save the dataframe to a new csv file

import pandas as pd

df = pd.read_csv("data/ruta_medellin_2025/race_results_general_sorted.csv")

# calculate the rank of each rider on each segment
df["rank_general_percentile"] = (df["Total Secs"].rank(method='first', pct=True) * 100).round(2).astype(float)
df["rank_segment_1"] = df["Segment 1 Secs"].rank(method='first').astype(int)
df["rank_segment_1_percentile"] = (df["Segment 1 Secs"].rank(method='first', pct=True) * 100).round(2).astype(float)
df["rank_segment_2"] = df["Segment 2 Secs"].rank(method='first').astype(int)
df["rank_segment_2_percentile"] = (df["Segment 2 Secs"].rank(method='first', pct=True) * 100).round(2).astype(float)
df["gain/loss_segment_2"] = df["rank_segment_2"] - df["rank_segment_1"]
df["rank_segment_3"] = df["Segment 3 Secs"].rank(method='first').astype(int)
df["rank_segment_3_percentile"] = (df["Segment 3 Secs"].rank(method='first', pct=True) * 100).round(2).astype(float)
df["gain/loss_segment_3"] = df["rank_segment_3"] - df["rank_segment_2"]

# save the dataframe to a new csv file
df.to_csv("data/ruta_medellin_2025/race_results_general_sorted_with_rank_progression.csv", index=False)

# select the following riders 858,882 and 1014, transpose the dataframe and print the results in a nice format to compare the results
df_selected = df[df["Number"].isin([858, 3726, 2583, 594])]
print(df_selected.transpose())


