# Importing math function
import math

# Welcome message
print("-------------------------------------------")
print("Welcome to the Quadratic Formula Calculator")
print("-------------------------------------------")

# Asking for inputs
a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
c = float(input("Enter a value for c: "))

# Applying the formula
x_1 = (-b + math.sqrt(math.pow(b,2) - 4*a*c))/ (2*a)
x_2 = (-b - math.sqrt(math.pow(b,2) - 4*a*c))/ (2*a)

# Printing the result
print(f"X1 ={x_1}\nX2 ={x_2}")