import random

class BotPlayer:
    def __init__(self, name):
        # Initialize the bot with 100 life points and default strength
        self.name = name
        self.life_points = 100
        self.strength = 0
    
    def set_strength(self):
        # Generate random strength between 1 and 20
        self.strength = random.randint(1, 20)
        return self.strength
    
    def receive_damage(self, damage):
        # Reduce life points by damage amount
        self.life_points -= damage
        if self.life_points < 0:
            self.life_points = 0
    
    def is_alive(self):
        # Check if bot is still alive
        return self.life_points > 0
    
    def get_strength(self):
        # Return current strength
        return self.strength
    
    def get_life_points(self):
        # Return current life points
        return self.life_points
    
    def __str__(self):
        # String representation of the bot
        return f"{self.name} Life Points: {self.life_points}"

def battle(attacker, defender):
    # Simulate a battle between two bots
    # Set strengths for both bots
    attacker_strength = attacker.set_strength()
    defender_strength = defender.set_strength()
    
    # Calculate damage (difference in strengths)
    if attacker_strength > defender_strength:
        damage = attacker_strength - defender_strength
        defender.receive_damage(damage)
        print(f"{attacker.name} strength: {attacker_strength}, {defender.name} strength: {defender_strength}.  "
              f"{defender.name} has {damage} points of damage.")
        return True  # Attacker won
    elif defender_strength > attacker_strength:
        damage = defender_strength - attacker_strength
        attacker.receive_damage(damage)
        print(f"{attacker.name} strength: {attacker_strength}, {defender.name} strength: {defender_strength}. "
              f"{attacker.name} you have {damage} points of damage.")
        return False  # Defender won
    else:
        print(f"{attacker.name} strength: {attacker_strength}, {defender.name} strength: {defender_strength}.  "
              f"It's a tie! No damage this round.")
        return None  # Tie

def main():
    """Main game function"""
    print("Welcome to Weber's Battle of the Bots!")
    print("-" * 40)
    
    # Create two bot objects
    bot1 = BotPlayer("Bot1")
    bot2 = BotPlayer("Bot2")
    
    # Track whose turn it is (True = Bot1's turn, False = Bot2's turn)
    bot1_turn = True
    round_num = 1
    
    # Display initial life points
    print(bot1)
    print(bot2)
    print()
    
    # Game loop
    while bot1.is_alive() and bot2.is_alive():
        if bot1_turn:
            current_bot = bot1
            opponent = bot2
            print(f"Bot{round_num} Your Turn!")
        else:
            current_bot = bot2
            opponent = bot1
            print(f"Bot{round_num} Your Turn!")
        
        # Get user input
        while True:
            action = input("Press h to hit, q to quit: ").lower().strip()
            if action == 'h' or action == 'q':
                break
            print("Invalid input. Please press 'h' to hit or 'q' to quit.")
        
        if action == 'q':
            print("\nNice battle!")
            # Determine winner
            if bot1.life_points > bot2.life_points:
                print("Bot1 wins this round!")
            elif bot2.life_points > bot1.life_points:
                print("Bot2 wins this round!")
            else:
                print("It's a tie!")
            print("Thanks for playing!")
            return
        
        # Perform battle
        print()
        battle(current_bot, opponent)
        print()
        
        # Display current life points
        print(bot1)
        print(bot2)
        print()
        
        # Switch turns
        bot1_turn = not bot1_turn
        round_num += 1
    
    # Game ended because a bot died
    print("\nNice battle!")
    if bot1.is_alive():
        print("Bot1 wins this round!")
    else:
        print("Bot2 wins this round!")
    print("Thanks for playing!")
main()