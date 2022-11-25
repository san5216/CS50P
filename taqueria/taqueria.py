

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total = 0

while True:

    try:
        key = input("What would you like? ").title()

        if key in menu:
            x = menu.get(key)
            total = total + x
            price = "Total: ${:.2f}"
            print(price.format(total))
        else:
            continue

    except KeyError:
        pass

    except EOFError:
        print("\n")
        break


