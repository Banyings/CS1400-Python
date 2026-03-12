# Import library
import random

# Initialize dictionary to store results
results = {}

print("Welcome to the dice throwing simulator!")

# Get user input
num_rolls = int(input("How many dice rolls would you like to simulate?: "))

# Simulate dice rolls
for _ in range(num_rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    
    if total not in results:
        results[total] = 1
    else:
        results[total] += 1

# Display results
print("\nDICE ROLLING SIMULATION RESULTS")
print(f"Total number of rolls = {num_rolls}")

# Print results for all possible sums (2-12)
for num in range(2, 13):
    count = results.get(num, 0)
    print(f"{num}: {count}")

# Bonus: Histogram showing percentages
print("\nHistogram showing percentages")
print()
# Theoretical probabilities for two dice
# Number of ways to roll each sum: 2(1), 3(2), 4(3), 5(4), 6(5), 7(6), 8(5), 9(4), 10(3), 11(2), 12(1)
# Total possible outcomes: 36

for num in range(2, 13):
    # Calculate theoretical percentage based on probability
    if num == 2 or num == 12:
        ways = 1
    elif num == 3 or num == 11:
        ways = 2
    elif num == 4 or num == 10:
        ways = 3
    elif num == 5 or num == 9:
        ways = 4
    elif num == 6 or num == 8:
        ways = 5
    else:  # num == 7
        ways = 6
    
    percentage = (ways / 36) * 100
    stars = int(percentage)  # Each * represents 1%
    print(f"{num}: {'*' * stars}")

print("\nThank you for using the dice throwing simulator. Goodbye!")