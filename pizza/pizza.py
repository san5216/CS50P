from tabulate import tabulate
import sys
import csv

filename = sys.argv[1]


table = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try:
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            table.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")

#print(table)

print(tabulate(table, headers="firstrow", tablefmt="grid"))