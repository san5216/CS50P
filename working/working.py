import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = re.search(r"^(([0-9][0-2]?):?([0-5][0-9])?) (AM|PM) to (([0-9][0-2]?):?([0-5][0-9])?) (AM|PM)$", s)

    if pattern:
        matches = pattern.groups()
        if int(matches[1]) > 12 or int(matches[5]) > 12:
            raise ValueError
        starting_time = set_time(hour=matches[1], minute=matches[2], am_pm=matches[3])
        ending_time = set_time(hour=matches[5], minute=matches[6], am_pm=matches[7])
        return f"{starting_time} to {ending_time}"
    else:
        raise ValueError


def set_time(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute is None:
        new_min = ":00"
        new_time = f"{new_hour:02}{new_min}"
    else:
        new_time = f"{new_hour:02}:{minute}"

    return new_time


if __name__ == '__main__':
    main()
