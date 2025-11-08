# There's a small fruit shop nearby your house that you like to buy from. Since you buy several
# fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily 
# you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many 
# of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5


def main():
    inventory = {
        "apple": 1.99,
        "melon": 3.99,
        "banana": 2.99,
        "kiwi": 1.99,
        "orange": 2.99,
        "mango": 1.99
    }
    total = 0
    for fruit, price in inventory.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total += quantity * price
    print(f"Your total is ${total:.2f}")
main()
        
        