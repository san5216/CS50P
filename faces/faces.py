def main ():
    faces = input("")
    faces = convert(faces)
    print(faces)


#convert :) and :(
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()
