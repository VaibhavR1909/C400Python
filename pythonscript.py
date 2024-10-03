import requests
import csv
from collections import Counter

url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

r= requests.get(url)

csvfile = 'taxi_zone_lookup.csv'

with open(csvfile, 'wb') as file:
    file.write(r.content)

with open(csvfile, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  
    data = list(reader)  

total_records = len(data)

uniqueborough = sorted(set(row[1] for row in data))

count = 0
for row in data:
    if row[1] == 'Brooklyn':
        count += 1


output_file = '/root/taxi_zone_output.txt'
with open(output_file, 'w') as f:
    f.write(f"Total Records: {total_records}\n")
    f.write(f"Unique Boroughs: {uniqueborough}\n")
    f.write(f"Records for Brooklyn: {count}\n")

print(f"Data saved to {output_file}")
