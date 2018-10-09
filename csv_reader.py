import csv
import os
from datetime import datetime
import collections

filename = "Crimes.csv"
fullname = os.path.dirname(__file__) + '/' + filename

if not os.path.isfile(fullname):
    exit(-1)

csv_file = csv.DictReader(open(fullname))

list_crimes = []
for line in csv_file:
    dt = datetime.strptime(line["Date"], '%m/%d/%Y %I:%M:%S %p')
    if dt.year == 2015:
        list_crimes.append(line["Primary Type"])

count = collections.Counter(list_crimes)
print(count)