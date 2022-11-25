import sys



lines = []
line_count = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")



if sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:

        for line in file:
            lines.append(line.lstrip())
            while ("" in lines):
                lines.remove('')

except FileNotFoundError:
    sys.exit("File does not exist")

for line in lines:
    if line.startswith("#"):
        pass
    else:
        line_count += 1

print(line_count)
