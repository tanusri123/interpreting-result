import csv
import pandas as pd

row=[]
with open('main.csv','r') as f:
    csvreader = csv.reader(f)
    for rows in csvreader:
        rows.append(row)

header = rows[0] 
planet_data_rows = rows[1:]
print(header)
print(planet_data_rows[0])