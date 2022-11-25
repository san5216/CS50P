import inflect

p = inflect.engine()
name = []
while True:

    try:
        x = input("")
        name.append(x)
        pass

    except EOFError:
        break

print("Adieu, adieu, to", p.join(name))