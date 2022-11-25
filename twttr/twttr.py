text = input("Input: ")

for _ in 'AEIOUaeiou':
    text = text.replace(_, "")

print("Output: ", text)