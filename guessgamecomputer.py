import random

# function to guess the number
def guess_game(x):
    # print welcome message
    print("\n Welcome to  Guess the Number Game ❤️")
    
    # pick a random number
    secret_number = random.randint(1, x)
    
    # initialize the guess number
    guess_number = 0
    
    while guess_number != secret_number:

    # Ask the player for a guess
        guess_number = int(input(f"\n Guess number between 1 to {x}:🤔 "))
# Check if the guess is correct
        if guess_number < secret_number:
            print("\n Too low. Guess again. 😒")

        elif guess_number > secret_number:
            print("\n Too high. Guess again. 🫡")
    
        else:
            print(f"\n Wow! congrate 👏 You guessed it right! {guess_number} 😍😍 ")


guess_game(10)
    
