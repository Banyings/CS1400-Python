# Import Random 
import random

# Print the Welcome Message
print("Stuck in the Mud")

# Set the score to zero
score = 0
# Fixing the list size with 5 dice
dice_to_roll = 5

while True:
    # Ask user to continue
    choice = input("Press r to roll or q to quit: ")

    if choice == "q":
        break

    # Roll the dice
    roll = []
    for i in range(dice_to_roll):
        roll.append(random.randint(1, 6))
    print(f"You rolled: {roll}")

    # Check each die
    for d in roll:
        if d == 2 or d == 5:
             # This die is stuck
            dice_to_roll -= 1 
        else:
            # Add to score
            score += d  

    print(f"Score: {score}")

    # Check if game is over
    if dice_to_roll == 0:
        print("All dice are stuck! Round ended.")
        break

print("Thanks for playing")
