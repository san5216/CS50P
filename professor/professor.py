import random


def main():

    level = get_level()
    score = keep_score(level)
    print("Score: ", score)


def get_level():



    while True:

        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass

    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x,y

def make_math(x, y):

    tries = 1

    while tries <= 3:
            answer = int(input(f"{x} + {y} = "))

            try:

                if answer == (x + y):
                    return True
                else:
                    tries += 1
                    print("EEE")
            except:
                tries += 1
    print(f"{x} + {y} = {x + y}")
    return False

def keep_score(level):

    problems = 1
    score = 0

    while problems <= 10:
        x, y = generate_integer(level)
        answer = make_math(x, y)
        if answer == True:
            score += 1
        problems += 1
    return score



if __name__ == "__main__":
    main()
