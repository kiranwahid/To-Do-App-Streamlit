# This program counts the number of times each number appears in a list. It uses a dictionary 
# to keep track of the information.
# An example run of the program looks like this (user input is in blue):
# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3
# Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

def count_numbbers():
    
    user_input = input("Enter a number: ")
    num_dict = {}
    while user_input != "":
        if user_input in num_dict:
            num_dict[user_input] += 1
        else:
            num_dict[user_input] = 1
        user_input = input("Enter a number: ")
    for key in num_dict:
        print(f"{key} appears {num_dict[key]} times.")
        
count_numbbers()

   
    