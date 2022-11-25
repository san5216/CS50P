import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    """Count the number of times 'um' appears in a string

    :param s: text string
    :return: int number
    """

    pattern = r"\bum"
    matches = re.findall(pattern, s)

    total = 0
    for match in matches:
        total += 1

    return total


if __name__ == "__main__":
    main()
