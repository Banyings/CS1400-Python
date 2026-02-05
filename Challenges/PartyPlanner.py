'''
Course: CS1400 - Python Programming
Instructor:	Kim Murphy
Author: Hyppolite Banyingela
Date: 2026-02-03
Title: Dinosaur Park Party Planner
'''
# Welcome to the Dinosaur Park Party Planner!
print("Welcome to the Dinosaur Park Party Planner!")

# While loop to keep the code run and quit when we enter 3
while True:
    print("\nSelect party type")
    print("1. Birthday Party")
    print("2. General Admission Group Party")
    print("3. Quit")
    choice = input("Enter choice: ")

    # If statement to check the conditions
    # I  made the choice a string because everytime I use an int, it runs the loop
    if choice == str(1):
        # Asking user if they are a member of the park
        membership = input("Are you a park member? (yes/no): ")

        # Asking the number of participants/ Adults and Kids
        adults_num = int(input("Number of adults: "))
        children_num = int(input("Number of children: "))

        if membership == "yes":
            base_price = 120  # Membership price
        else:
            base_price = 150  # Non-membership price
        extra_guest = max(0, (adults_num + children_num) - 12)
        extra_guest_price = extra_guest * 3

        # Print results for both cases
        print(f"\nBase party price: ${base_price}")
        print(f"Extra guests:        {extra_guest}")
        print(f"Extra guest cost:   ${extra_guest_price}")
        print(f"Total price:      ${base_price + extra_guest_price}")

    elif choice == str(2):  # General Admission Group Party
        adults_num = int(input("Number of adults: "))
        children_num = int(input("Number of children: "))

        total_price_group = (adults_num * 5) + (children_num * 4)
        print(f"The total price is: ${total_price_group} ")
        print(f"You are being charged $5 per adult(13+)\n"
              f"and $4 for children(2-12). Enjoy your\n"
              f"party!!!!!")

    elif choice == str(3):
        quit()



