# 🚀 Password Generator Project
# 🎲 This allows us to pick random things!
import random  
 # 🔡 This helps us with letters, numbers, and symbols!
import string 

# 🎉 A friendly welcome message for the user
print("\n Welcome to the Password Generator! 🎉")

# 🅰️ Letters: Includes both uppercase and lowercase letters (A-Z and a-z)
letters = string.ascii_letters

# 🔢 Numbers: Digits from 0 to 9
numbers = string.digits

# 🔣 Symbols: Special characters like !, @, #, $, etc.
symbols = string.punctuation

# ➕ Combine letters, numbers, and symbols to form a pool of characters
combined_characters = letters + numbers + symbols

# 🧑‍💻 Ask the user how long they want their password to be
user_input = int(input("How many characters would you like in your password 🔣? "))

# 🎲 Generate a random password by picking characters from the combined pool
# We'll pick 'user_input' number of characters
password = ' '.join(random.choice(combined_characters) for i in range(user_input))

# 📝 Show the generated password to the user
print(f"\n Your password is: {password}")

# 🎉 End of Password Generator Project
print("\n Thank you for using the Password Generator!👋")

