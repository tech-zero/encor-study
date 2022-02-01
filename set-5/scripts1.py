import csv


with open("spreadsheet1.csv", "r") as csv_data:
    csv_reader = csv.reader(csv_data)
    print(csv_reader)  # Reads the data and not the header
    for line in csv_reader:
        print(line)

print("\n")

with open("spreadsheet1.csv", "r") as csv_data:
    csv_reader = csv.reader(csv_data)
    # print(csv_reader)  # Reads the data and not the header
    for line in csv_reader:
        print(line[2])


"""
with open('spreadsheet1.csv', 'r') as csv_data:
    csv_reader = csv.reader(csv_data)
    print(csv_data)
    print(csv_reader)  # Prints out reader object and it's position in memory
    for line in csv_reader:
        print(line)
"""
