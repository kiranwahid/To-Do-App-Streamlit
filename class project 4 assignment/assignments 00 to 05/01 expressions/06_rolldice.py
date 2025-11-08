# Simulate rolling two dice, and prints results of each roll as well as the total.

import random


limit:int = 6
def roll_dice():
    # Define a function to simulate rolling a single die.
    # Use randint to get an integer between 1 and 6
    dice1 = random.randint(1, limit)
    dice2 = random.randint(1,limit)
    total = dice1 + dice2
    return dice1, dice2, total

# Looping over the dice rolls.
for i in range(2):
    dice1, dice2, total = roll_dice()  # Call the function with parentheses
    print(f"Rolling dice: Dice1: {dice1}, Dice2: {dice2}, Total: {total}")
  
    
    