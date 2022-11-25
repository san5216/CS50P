def main():

    text = input("Input: ")
    letters = shorten(text)
    print("Output: ", letters)

def shorten(text):
    letters = ""
    for letter in text:
        if not letter in 'AEIOUaeiou':
            letters += letter
    return letters




if __name__ == "__main__":
    main()