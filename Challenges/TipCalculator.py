# Printing Tip Calculator
print("_______________")
print("\nTip Calculator")
print("_______________")

# Asking for the cost of the meal and service quality
cost = float(input("Enter the cost of your meal: "))
service = input("How was the service? (Excellent, Good, Poor): ")

# Determining the tip percentage based on service quality
percentage = .10

# Asking user for feedback
if service == "Excellent" or service == "Good":
    percentage += .10
else:
    percentage += .05

# Calculating the tip and total cost
tip = cost * percentage
cost += tip

# Displaying the tip and total cost
print(f"Tip: ${tip:.2f}")
print(f"Cost: ${cost:.2f}")