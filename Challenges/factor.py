# Display Factors of all the numbers
print("-----------------------------------")
print("Print all the factors of any number")
print("-----------------------------------")

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Using while loop to run the code over and over as soon as the user enters a new number
while num > 0:
    # Display Factors
    print(f"The factors of {num} are:", end = "")
    for i in range(1, num+1):
        if num % i == 0:
            print(f" {i}", end = " ")
    print("") 
    print("")
    num = int(input("Enter a number or -1 to exit: "))
