import sys
import csv

before = []
output = []



if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1], "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            split_name = row["name"].rstrip().split(", ")
            output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")



with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writerow({"first": "first", "last": "last", "house": "house"})
    for row in output:
        writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
