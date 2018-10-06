import os

filename = "dataset_24465_4.txt"
fullname = os.path.dirname(__file__) + '/' + filename

resultname = "dataset.txt"
fullResultName = os.path.dirname(__file__) + '/' + resultname

if not os.path.isfile(fullname):
    exit(-1)

with open(fullname) as file:
    lines = [line for line in file]

lines.reverse()

outF = open(fullResultName, "w")
outF.writelines(lines)
outF.close()

print('Ok!')