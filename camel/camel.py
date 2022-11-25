camel = input("VariableName: ")
for c in camel:
    if c.isupper() == True:
        c = c.replace(c, "_" + c).lower()
        print(c, end="")
    else:
        print(c, end="")
print()

# 1
 #2
# 3