import sys
import os
from PIL import Image, ImageOps

def main():

    valid_arguments()
    second = valid_output()
    muppet = get_input()
    shirt = get_shirt()
    muppet = resize_before(muppet)
    muppet.paste(muppet, shirt)
    print(sys.argv[2], second)
    muppet.save(sys.argv[2], format=second)

def valid_output():

    good_files = ["jpg", "jpeg", "png"]

    first = os.path.splitext(sys.argv[1])
    second = os.path.splitext(sys.argv[2])

    for ext in good_files:
        if ext.lower() not in good_files :
            sys.exit("Invalid output")

    if first[1] != second[1]:
        sys.exit("Input and output have different extensions")

    return second

def valid_arguments():
    if len(sys.argv) > 3:
        sys.exit("Too many command arguments")
    elif len(sys.argv) < 3:
        sys.exit("too few command arguments")
    else:
        return True


def get_shirt():
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    return shirt

def get_input():
    muppet = Image.open(sys.argv[1])
    return muppet

def resize_before(muppet):
    shirt = get_shirt()
    shirt_size = shirt.size
    muppet = ImageOps.fit(shirt, shirt_size)
    return muppet


if __name__ == "__main__":
    main()
