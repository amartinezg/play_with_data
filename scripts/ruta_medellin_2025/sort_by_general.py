import pandas as pd

df = pd.read_csv("data/ruta_medellin_2025/race_results_by_category.csv")

df_sorted = df.sort_values(by="Total Secs")

df_sorted["rank_general"] = df_sorted["Total Secs"].rank(method='first').astype(int)

cols = df_sorted.columns.tolist()
try:
    category_rank_index = cols.index("CategoryRank")
    cols.pop(cols.index("rank_general"))
    cols.insert(category_rank_index + 1, "rank_general")
except ValueError:
    cols.pop(cols.index("rank_general"))
    cols.insert(1, "rank_general")

df_sorted = df_sorted[cols]

df_sorted.to_csv("data/ruta_medellin_2025/race_results_general_sorted.csv", index=False)
print("Data sorted by total time with general rank added, and saved to data/ruta_medellin_2025/race_results_general_sorted.csv")