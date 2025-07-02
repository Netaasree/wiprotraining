import csv
with open("people.csv", 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name","age"])
    for _ in range(10):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        writer.writerow([name,age])
print("Data written on csv file")