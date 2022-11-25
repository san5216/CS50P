greeting = input("Greeting: ").strip().lower()

if greeting[:5] == "hello":
    print("$0")
elif greeting[0] != "h":
    print("$100")
else:
    print("$20")
