# Importing the random module to generate a random number
import random  

# Function to play the game
def play_game():
    print("\nWelcome to Guess the Number Game ❤️")

    # Generate a secret number between 50 and 100
    secret_number: int = random.randrange(50, 100)

    # Set the total number of attempts the player has
    attempt: int = 7

    # Initialize guess_number to track the number of attempts the player has made
    guess_number: int = 0

    # Start the loop for the guessing game
    while guess_number < attempt:
        # Increase the guess count after each guess
        guess_number += 1
        
        # Get user input, converting it to an integer
        user_gues = int(input("Enter a guess between 50 to 100:🤔 "))
        
        # Check if the user's guess is equal to the secret number
        if user_gues == secret_number:
            print(f"\nWow! Congrats 👏 You guessed it right in {guess_number} attempts 😍😍")
            break  # Exit the loop since the correct guess has been made
        
        # If the user has used all attempts and hasn't guessed correctly
        elif guess_number >= attempt and user_gues != secret_number:
            print(f"Oops, the correct number was {secret_number}😒 ")
        
        # If the guess is less than the secret number (too low)
        elif user_gues < secret_number:
            print("\nToo low. Guess again. 😒")
        
        # If the guess is greater than the secret number (too high)
        elif user_gues > secret_number:
            print("\nToo high. Guess again. 🫡")

# Main loop to ask if the user wants to play again
while True:
    play_game()  # Call the function to play the game
    
    # Ask the user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    
    # Check if the user says 'no', and break the loop if they don't want to continue
    if play_again != "yes":
        print("\nThank you for playing! Goodbye! 👋")
        break
