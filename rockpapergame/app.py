import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Choose: 🪨 rock, 📄 paper, ✂️ scissors: \n").lower()
        computer_choice = random.choice(choices)

        if user_choice not in choices:
            print("Invalid choice. Please try again! 🤔")
            continue

        print(f"\nYou chose: {user_choice.capitalize()} 🧑")
        print(f"Computer chose: {computer_choice.capitalize()} 💻")

        if user_choice == computer_choice:
            print("It's a tie! 😐 You both chose the same.")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win!")
        else:
            print("😔 Computer wins!")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! 👋")
            break

rock_paper_scissors()
