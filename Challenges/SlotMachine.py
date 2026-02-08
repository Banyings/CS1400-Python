'''
Course: CS1400 - Python Programming
Instructor:	Kim Murphy
Author: Hyppolite Banyingela
Date: 2025-02-07
Title: Murph E Cheese Slot Machine
'''
# import math
import random
print("Murph E Cheese Slot Machine")
print()  # Empty line for spacing
tokens = int(input("Enter the starting number of tokens you wish to use: "))

while True:
    bet = int(input("How much do you wish to bet? (4 to cash out): "))

    # Handle cash out
    if bet == 4:
        print(f"You received {tokens} tokens")
        print("Thanks for playing")
        break

    # Generate random numbers (1-5)
    num_one = random.randint(1, 5)
    num_two = random.randint(1, 5)
    num_three = random.randint(1, 5)

    print(f"[{num_one}] [{num_two}] [{num_three}]")

    # Check if all numbers are the same (win condition)
    if num_one == num_two == num_three:
        # Calculate winnings: number rolled to the power of bet
        win_amount = pow(num_one, bet)
        tokens += win_amount
        print("Congratulations")
        print(f"You win {win_amount} tokens")
        print(f"Tokens: {tokens}")
    
    else:
        # Player loses their bet
        tokens -= bet
        print(f"You lose {bet} tokens")
        print(f"Tokens: {tokens}")

    # Check if player has run out of tokens
    if tokens <= 0:
        print("You're out of tokens! Game over.")
        break