import random

class CootieCatcher:
    def __init__(self):
        # List of 8 possible messages
        self.messages = [
            "Positively Not",
            "Definitely Yes",
            "Ask Again Later",
            "Very Doubtful",
            "Without a Doubt",
            "Better not tell you now",
            "Yes, in time",
            "No, never"
        ]
        self.final_message = ""

    def makeChoice(self):
        # Step 1: Color choice
        valid_colors = ["red", "yellow", "green", "blue"]
        while True:
            color = input("Choose a color(red, yellow, green, blue): ").lower()
            if color in valid_colors:
                break
            else:
                print("Sorry that is not an option")

        # Determine number set based on color length parity
        if len(color) % 2 == 0:  # even length (blue=4, yellow=6)
            number_options = [1, 2, 5, 6]
        else:  # odd length (red=3, green=5)
            number_options = [3, 4, 7, 8]

        # Number choice
        while True:
            try:
                number = input(f"Choose a number{tuple(number_options)}: ")
                # Check if input is a number
                if not number.isdigit():
                    print("Sorry that is not a number. Please enter your choice in numeric format.")
                    continue
                number = int(number)
                if number in number_options:
                    break
                else:
                    print("Sorry that is not an option")
            except ValueError:
                print("Sorry that is not a number. Please enter your choice in numeric format.")

        # Step 4: Use number to pick a message from the list
        # Map the number to an index in messages list
        index = number - 1
        self.final_message = self.messages[index]
        return self.final_message

# Main game loop
print("Welcome to Cootie Catcher")

play_again = True
while play_again:
    question = input("Ask your Cootie Catcher a question: ")
    
    # Create object of the class
    c = CootieCatcher()
    
    # Get the final message
    result = c.makeChoice()
    print(f"Cootie says: {result}")
    
    # Ask to play again
    while True:
        choice = input("Would you like to (p)lay again or (q)uit? ").lower()
        if choice == 'q':
            play_again = False
            break
        elif choice == 'p':
            break
        else:
            print("Please enter 'p' to play again or 'q' to quit.")

print("Thanks for playing!")