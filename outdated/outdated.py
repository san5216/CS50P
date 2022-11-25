months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
m = 0
d = 0
y = 0

while True:
    try:
        date = input("Date: ")

        if date[0].isdigit():
            m, d, y = date.split("/")

            m = int(m)
            d = int(d)
            y = int(y)

            if m > 12 or d > 31:
                raise ValueError
            else:
                print(f"{y}-{m:02}-{d:02}")
                break

        else:
            if date[0].isalpha():
                m, d, y = date.split(" ")

                if date[-6] == ",":
                    d = d.strip(",")
                else:
                    raise ValueError


                m = months.index(m)

                m = int(m) + 1
                d = int(d)
                y = int(y)

                if m > 31 or d > 12:
                    raise ValueError
                else:
                    print(f"{y}-{m:02}-{d:02}")
                    break

    except ValueError:
        pass

