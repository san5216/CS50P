from datetime import date, datetime
import sys
import inflect

p = inflect.engine()


def main():
    birthdate = input("Date of Birth: ")

    days = date_difference(dob=birthdate).days

    minutes = (days*24)*60

    words = p.number_to_words(minutes, andword="").capitalize()

    print(f"{words} minutes")


def date_difference(dob):
    now = date.today()

    try:
        birthdate = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")

    return now - birthdate


if __name__ == "__main__":
    main()
