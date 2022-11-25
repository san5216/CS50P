import random
import sys

level = 0
guess = 0

while True:

    try:
        level = input("Level: ")
        level = int(level)
        level = random.randrange(1, level)

        break

    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))

        if guess < level:
            print("Too small!")
            pass
        elif guess > level:
            print("Too large!")
            pass
        else:
            sys.exit("Just right!")

    except ValueError:
        pass

