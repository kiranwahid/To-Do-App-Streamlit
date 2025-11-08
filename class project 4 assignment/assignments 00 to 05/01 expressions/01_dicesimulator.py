import random

def roll_dice():
    # Define a function to simulate rolling a single die.
    dice1 = random.randint(1, 6)  # Use randint to get an integer between 1 and 6
    dice2 = random.randint(1, 6)
    return dice1, dice2

# Looping over the dice rolls.
for i in range(3):
    dice1, dice2 = roll_dice()  # Call the function with parentheses
    print(f"Rolling dice: Dice1: {dice1}, Dice2: {dice2}")
