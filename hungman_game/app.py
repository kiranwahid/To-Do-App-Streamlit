import random

# 🍎🍇 Create a basket of different fruits
fruit_basket = ["apple", 'mango', 'banana', 'orange', 'cherry', 'grapes', 'pineapple', 'strawberry', 'kiwi', 'pear']

# 🎯 Randomly select one fruit from the basket
random_fruit = random.choice(fruit_basket)

# 🧩 Create blanks (underscores) for each letter in the random fruit, representing the word to guess
blanks = '_' * len(random_fruit)

# ❤️ Set the number of lives (chances) the player has to guess the fruit
lives = 10

# 🎮 Start the guessing loop - Keep going until the player runs out of lives or guesses the word
while lives > 0 and "_" in blanks:
    # ✏️ Display the current status of the guessed word with blanks
    print("Guess a letter: " + " ".join(blanks))
    
    # 🧐 Prompt the player to enter a letter and make sure it's lowercase
    guess = input("Enter a letter: ").lower()
    
    # ✅ If the guessed letter is in the fruit, reveal the letter in the correct position(s)
    if guess in random_fruit:
        for i in range(len(random_fruit)):
            if random_fruit[i] == guess:
                # 💡 Replace the blank with the correct letter
                blanks = blanks[:i] + guess + blanks[i+1:]
    
    # ❌ If the guessed letter is not in the fruit, reduce the number of lives
    else:
        lives -= 1
        print(f"Oops! {guess} is not in the word. Lives left: {lives} 💔")

    # 🏆 Check if all blanks have been filled, meaning the player has won
    if "_" not in blanks:
        print(f"You win! 🎉 The fruit was: {random_fruit} 🍓")
    # 😢 If no lives are left, the player loses the game
    elif lives == 0:
        print(f"You lose! 😔 The fruit was: {random_fruit} 🍌")



