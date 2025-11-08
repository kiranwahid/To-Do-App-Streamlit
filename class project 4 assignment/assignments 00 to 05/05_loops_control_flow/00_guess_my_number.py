# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# Play again? (yes or no)


import random

def play_game():
    number = random.randint(0, 99)
    guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))
    while guess != number:
        if guess > number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        guess = int(input("Enter a new number: "))
    print(f"Congrats! The number was: {number}")
    play_again = input("Play again? (yes or no) ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("\nThank you for playing! 😊😊 Goodbye.👋")
if __name__ == "__main__":
    play_game()