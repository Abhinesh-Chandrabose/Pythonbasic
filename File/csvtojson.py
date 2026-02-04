import csv
import json
data =[]
with open("student.csv","r",newline="") as csvfile:
    filedata = csv.DictReader(csvfile)
    for r in filedata:
        data.append(r)
with open ("student.json","w") as jsonfile:
    json.dump(data,jsonfile,indent=4)