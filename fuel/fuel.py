def main():

    fuel_fraction = get_fuel_level("How much gas is in the tank? ")

    if fuel_fraction <= 1:
        print("E")
    elif fuel_fraction >= 99:
        print("F")
    else:
        print(round(fuel_fraction), "%", sep="")


def get_fuel_level(fuel):
    while True:
        try:
            fuel = input(fuel).split("/")

            x = int(fuel[0])
            y = int(fuel[1])

            try:
                if x <= y:
                    fuel_fraction = (x / y) * 100
                    return fuel_fraction
            except:
                break

        except (ValueError, ZeroDivisionError):
            pass


main()