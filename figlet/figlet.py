from pyfiglet import Figlet
import sys, random

figlet = Figlet()

fonts_list = figlet.getFonts()
#print(sorted((fonts_list)))

# If there are no arguments, print output in random font
if len(sys.argv) == 1:
    f = random.choice(fonts_list)
    figlet.setFont(font=f)

    s = input("Input: ")
    print("Output:\n")
    print(figlet.renderText(s))


elif len(sys.argv) == 3:

    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet.setFont(font=sys.argv[2])
        s = input("Input: ")

        if sys.argv[2] in fonts_list:
            print("Output:\n")
            print(figlet.renderText(s))
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")


