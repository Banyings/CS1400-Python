'''
Course: CS1400 - Python Programming
Instructor:	Kim Murphy
Author: Hyppolite Banyingela
Date: 2025-01-19
Title: Driving Costs
'''

# I'm printing an empty line for a better user experience
print("------------------------------------------------")
# Asking User to enter The number of miles to the gallon their vehicle get
milesPerGallon = float(input("How many miles to the gallon does your car get?: Area 1: "))
print("------------------------------------------------")

# Asking User to enter the current cost of gas
gasPrice = float(input("What is the current cost of gas?: "))
print("------------------------------------------------")


# Asking User to enter the name of the first, second, and third area
firstArea = input("What is the current area you would like to calculate the cost to? Area 1: ")
secondArea = input("What is the current area you would like to calculate the cost to? Area 2: ")
thirdArea = input("What is the current area you would like to calculate the cost to? Area 3: ")
print("------------------------------------------------")

# Asking User to enter the distance from the fist, second, and third area to Weber State University
distanceOne = float(input("How many miles is it to your first area from Weber State? Area 1: "))
distanceTwo = float(input("How many miles is it to your second area from Weber State? Area 2: "))
distanceThree = float(input("How many miles is it to your third area from Weber State? Area 3: "))
print("------------------------------------------------")

# calculating the cost to drive to the first area
costOne = (distanceOne / milesPerGallon) * gasPrice
costTwo = (distanceTwo / milesPerGallon) * gasPrice
costThree = (distanceThree / milesPerGallon) * gasPrice

# Rounding the cost
costOne = round(costOne, 2)
costTwo = round(costTwo, 2)
costThree = round(costThree, 2)

# Printing the cost to drive to the first area using the f-string
print(f"The Driving cost for area 1 {firstArea} is $ {costOne} ")
print(f"The Driving cost for area 2 {secondArea} is $ {costTwo} ")
print(f"The Driving cost for area 3 {thirdArea} is $ {costThree} ")

