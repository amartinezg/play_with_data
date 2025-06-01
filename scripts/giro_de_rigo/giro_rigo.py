import requests
import csv
import time

url = "https://finalap.com/api/list?eventId=el-giro-de-rigo-la-despedida-2024&track=Reto+Leyenda&sortColumn=posGeneral&sortOrder=asc&query=&page=1&limit=11000"
response = requests.get(url)
data = response.json()

# preview the data
print(data['results'][:10])

# Create CSV file with headers
headers = ['id', 'user_id', 'name', 'lastname', 'track', 'event', 'date', 'gender',
          'gun_time', 'chip_time', 'bib', 'country', 'age', 'delay', 'penalty',
          'average_km', 'status', 'team', 'category', 'pos_general', 'pos_category',
          'pos_gender', 'split_palmas', 'split_palmas_humanized','split_km33', 'split_km33_humanized',
          'split_raya', 'split_raya_humanized',
          'split_km119', 'split_km119_humanized',
          'split_final', 'split_final_humanized']

with open('data/giro_de_rigo_times.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for row in data['results']:
        # Extract split times
        splits = row['splitTimes']

        # Write row with all columns including splits
        # each split is in seconds, convert to humanized format (HH:MM:SS)
        split_palmas_humanized = time.strftime('%H:%M:%S', time.gmtime(splits[0]))
        split_km33_humanized = time.strftime('%H:%M:%S', time.gmtime(splits[3]))
        split_raya_humanized = time.strftime('%H:%M:%S', time.gmtime(splits[1]))
        split_km119_humanized = time.strftime('%H:%M:%S', time.gmtime(splits[4]))
        split_final_humanized = time.strftime('%H:%M:%S', time.gmtime(row['chipTime']))

        writer.writerow([
            row['id'], row['userId'], row['name'], row['lastname'], row['track'],
            row['event'], row['date'], row['gender'], row['gunTime'], row['chipTime'],
            row['bib'], row['country'], row['age'], row['delay'], row['penalty'],
            row['averageKm'], row['status'], row['team'], row['category'],
            row['posGeneral'], row['posCategory'], row['posGender'],
            splits[0], split_palmas_humanized, splits[3], split_km33_humanized,
            splits[1], split_raya_humanized, splits[4], split_km119_humanized,
            row['chipTime'], split_final_humanized
        ])
