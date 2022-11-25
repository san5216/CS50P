def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    number = len(s)
    if number < 2 or number > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    for c in s:
        if c.isalnum == False:
            return False

    return True

if __name__ == "__main__":
    main()