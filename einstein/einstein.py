# E=mc**2
# E equals energy in Joules
# m equals mass in kilograms
# c equals speed of light

# prompts user for mass as an interger in kg
# outputs the equivalent number of Joules as an interger
# Prints number of Joules to screen

m = (int(input("Mass in kg: ")))
c_squared = pow(300000000, 2)

joules = m * c_squared

print(joules)