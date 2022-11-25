def main():

    deepInput = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

    if deepInput == "42" or deepInput == "forty-two" or deepInput == "forty two":
        print("Yes")
    else:
        print("No")

main()