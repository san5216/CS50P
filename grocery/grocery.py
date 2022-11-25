list = {

}

count = 1

while True:
    try:
        item = input("").upper()

        if item in list:
            x = list.get(item)
            list.update({item: (x + 1)})
        else:
            list.update({item: count})

    except KeyError:
        pass

    except EOFError:
        break

for item in sorted(list):
    print(list[item], item)

