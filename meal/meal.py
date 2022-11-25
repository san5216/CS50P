def main():

    hours = convert(input("Time: "))

    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")


def convert(time):


        h, m = time.split(":")

        h == time[0]
        m == time[1]

        if " a.m." in m:
            m = m.removesuffix(" a.m.")
        elif " p.m." in m:
            m = m.removesuffix(" p.m.")
            h = float(h) + 12

        h = float(h)
        m = float(m)

        hours = h + (m / 60)

        hours = round(hours, 2)

        return hours




if __name__ == "__main__":
    main()