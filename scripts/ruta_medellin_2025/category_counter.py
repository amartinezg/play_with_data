import pandas as pd

df = pd.read_csv("data/ruta_medellin_2025/race_results_general_sorted.csv")

# count the number of riders in each category
category_counts = df["Category"].value_counts()
print(category_counts)

# save it to a csv file
category_counts.to_csv("data/ruta_medellin_2025/category_counts.csv", index=True)