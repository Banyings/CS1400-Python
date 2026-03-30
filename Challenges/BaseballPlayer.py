# create the BaseBallPlayer class
class BaseBallPlayer:
    def __init__(self):
        self.name = "none"
        self.number = "none"
        self.batting_avg = 0
    
    def calculate_batting_avg(self, incoming_hits, incoming_at_bats):
        self.batting_avg = round(incoming_hits/incoming_at_bats, 3)
        return self.batting_avg
# main program
print("Welcome to the Player Tracker!")
playerName = input("What is the player's name: ")
playerNumber = input("What is the player's number: ")

myPlayer = BaseBallPlayer()
myPlayer.name = playerName
myPlayer.number = playerNumber

hits = int(input("How many hits did the player get: "))
at_bats = int(input("How many attempts to hit the ball did the player get: "))
print("The average batting is: " + str(myPlayer.calculate_batting_avg(hits, at_bats)))

