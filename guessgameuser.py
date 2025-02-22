import random

def computer_guess(x):
    # Initialize the range in which the computer will guess
    low = 1
    high = x
    feedback = ''  # Variable to store user feedback

    # Continue guessing until the computer gets the correct answer ('c')
    while feedback != 'c':
        # If low and high are not the same, make a random guess between them
        if low != high:
            guess = random.randint(low, high)
        else:
            # If low and high are the same, the guess has to be that number
            guess = low

        # Ask the user if the guess is too high, too low, or correct
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        # Adjust the range based on the feedback
        if feedback == 'h':
            high = guess - 1  # Reduce the upper limit if the guess is too high
        elif feedback == 'l':
            low = guess + 1   # Increase the lower limit if the guess is too low

    # Once the correct guess is made, print a success message
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

# Start the game with the number range up to 20
computer_guess(20)
