# WELCOME TO IDENTIFIER CHECK
print("WELCOME TO PROPOSED VARIABLE NAME")

# While loop to run the command as long as it is different to q
while True:
    # Ask user to enter a variable name of choice
    name = input("Enter a variable name of your choice or (Enter q to quit): ")

    # Check for quit condition
    if name == "q":
        print("Thank you for your participation")
        break

    # Check if variable starts with a number (illegal)
    if name and name[0].isdigit():
        print("Illegal.")

    # Check if variable contains spaces (illegal)
    elif " " in name:
        print("Illegal.")

    # Check if variable contains only letters, numbers, and underscore (legal)
    elif name.isidentifier():
        print("Good!")

    # Check if variable contains special characters (legal, but poor style)
    else:
        print("Legal, but uses poor style.")