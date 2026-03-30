# Created the age check function to verify age
def check_age():
    first_attempt = True
    while True:
        try:
            if first_attempt:
                age = int(input("Enter age: "))
                first_attempt = False
            else:
                age = int(input("Re-enter age: "))
                
            if age <= 0:
                print("Invalid age. Must be positive.")
            else:
                return age
        except ValueError:
            if first_attempt:
                print("Invalid age. Must be a number.")
                first_attempt = False
            else:
                print("Invalid age. Must be a number.")

# Created the age heigh function to verify height
def check_height():
    first_attempt = True
    while True:
        try:
            if first_attempt:
                height = float(input("Enter height in inches: "))
                first_attempt = False
            else:
                height = float(input("Re-enter height in inches: "))
                
            if height <= 0:
                print("Invalid inches value. Must be positive.")
            else:
                return height
        except ValueError:
            if first_attempt:
                print("Invalid inches value. Must be a number.")
                first_attempt = False
            else:
                print("Invalid inches value. Must be a number.")

# Created the age weight function to verify weight
def check_weight():
    first_attempt = True
    while True:
        try:
            if first_attempt:
                weight = float(input("Enter weight in pounds: "))
                first_attempt = False
            else:
                weight = float(input("Re-enter weight in pounds: "))
                
            if weight <= 0:
                print("Invalid pounds value. Must be positive.")
            else:
                return weight
        except ValueError:
            if first_attempt:
                print("Invalid pounds value. Must be a number.")
                first_attempt = False
            else:
                print("Invalid pounds value. Must be a number.")

# Calculate BMI and Fat Burning Heart Rate 
def calculate_BMI_Fat(age, height, weight):
    BMI = round(((weight * 703) / (height ** 2)), 1)
    Fat_Burn = round(((220 - age) * 70/100), 1)
    
    print()
    print(f"Age = {age}")
    print(f"Height = {height}\"")
    print(f"Weight = {weight} pounds")
    print()
    print(f"Fat Burning Heart Rate = {Fat_Burn} bpm")
    print(f"Body Mass Index = {BMI}")

# Main function that calls age, height and weight
print("Welcome to the Weber State University Human Performance Lab!")
print("Please utilize the following calculator to find your ideal fat burning heart rate and BMI.\n")
print("The program will also store this information in a file you choose so that it can be tracked over time.")
    
    # Get all the values
age = check_age()
height = check_height()
weight = check_weight()
    
    # Calculate and display results
calculate_BMI_Fat(age, height, weight)

