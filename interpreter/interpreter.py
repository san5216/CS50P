x, y, z = input("Expression: ").split(" ")

x = float(x)
z = float(z)

if y == "+":
    y = round((x + z), 1)
    print(y)
elif y == "-":
    y = round((x - z), 1)
    print(y)
elif y == "/":
    y = round((x / z), 1)
    print(y)
else:
    y = round((x * z), 1)
    print(y)
