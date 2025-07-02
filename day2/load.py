import csv
with open("people.csv","r") as file:
    coder=csv.reader(file)
    for row in coder:
        print(row)
        