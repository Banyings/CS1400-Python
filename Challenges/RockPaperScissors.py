import random

class RockPaperScissors:
    def getUserChoice(self):
        # Get user's choice of Rock, Paper, or Scissors with input validation
        valid_choices = ["rock", "paper", "scissors"]
        
        while True:
            userChoice = input("Rock, Paper, or Scissors?: ").strip().lower()
            
            if userChoice in valid_choices:
                # Capitalize the first letter for consistent output
                return userChoice.capitalize()
            else:
                print(f"Sorry, \"{userChoice}\" is not a valid entry.")
    
    def getCPUChoice(self):
        # Randomly generate computer's choice of Rock, Paper, or Scissors
        choices = ["Rock", "Paper", "Scissors"]
        cpuChoice = random.choice(choices)
        return cpuChoice
    
    def pickWinner(self, userChoice, cpuChoice):
        # Determine the winner based on the choices
        # Convert to lowercase for comparison
        user_lower = userChoice.lower()
        cpu_lower = cpuChoice.lower()
        
        # Check for tie
        if user_lower == cpu_lower:
            return 0  # Tie
        
        # Check for user win conditions
        if (user_lower == "rock" and cpu_lower == "scissors") or \
           (user_lower == "paper" and cpu_lower == "rock") or \
           (user_lower == "scissors" and cpu_lower == "paper"):
            return 1  # User wins
        else:
            return 2  # Computer wins
#Main Program
rps = RockPaperScissors ()  #***YOUR CLASS

print("Welcome to Rock, Paper, Scissors!")

hasError = False
numUserWins = 0
numCPUWins = 0

while True:
    try:
        
        #Reset error checker
        hasError = False
        
        #Get odd number of games
        numGames = int(input("How many rounds would you like to play?: "))
        
        while numGames % 2 == 0: #Even number
        
            print("Sorry, number of games must be odd.  Please try again: ")
            numGames = int(input("How many rounds would you like to play?: "))
        
        break
        
    except ValueError as err:
        
        hasError = True
        
        print("Invalid input.  Please enter a number.")
        
		
#Play the game for the number of rounds the user entered allowing for ties with the count variable
count = 0
while count < numGames:

    #Get the user and computer choices
    userChoice = rps.getUserChoice()  #***YOUR METHOD
    cpuChoice = rps.getCPUChoice()   #***YOUR METHOD
    
    print("Computer choose is " + cpuChoice)
    
    #Pick winner
    winner = rps.pickWinner(userChoice, cpuChoice)  #***YOUR METHOD
    
    if winner == 0:
        print("It's a tie!  Play again.")
    elif winner == 1:
        print("User wins!")
        numUserWins+=1
        count += 1
    elif winner == 2:
        print("Computer wins!")
        numCPUWins+=1
        count += 1
    else:
        print("Error in picking winner!")
#Print results
print("\n\nUser wins: ", numUserWins)
print("Computer wins: ", numCPUWins)

if numUserWins > numCPUWins:

    print("The user won!")


if numCPUWins > numUserWins:

    print("The computer won!")


#Close game
print("\nThank you for playing!")
