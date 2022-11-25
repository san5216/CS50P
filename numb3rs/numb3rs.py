import re


def main():
    print(validate(input("IPv4 Address: ")))



def validate(ip):

    if re.search(r"^(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)(\d{1,3})$", ip):
        split_numbers = ip.split(".")
        for number in split_numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False




if __name__ == "__main__":
    main()
