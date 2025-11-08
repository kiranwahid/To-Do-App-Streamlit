# Write a program which continuously asks the user to enter values which are added one by one into a list. 
# When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


#  define function that will be called get_list
def get_list():
    # create an empty list to store the values
    list = []
    # while loop to keep asking the user for values until they press enter without typing anything
    while True:
        # ask the user to enter a value
        value = input("Enter a value: ")
        if value == "":
            # if the user presses enter without typing anything, break out of the loop
            break
        # add the value to the list
        list.append(value)
    # print the list
    print("Here's the list:", list)


#  define function that will be called get_list
def get_list():
    # create an empty list to store the values
    list = []
    # while loop to keep asking the user for values until they press enter without typing anything
    while True:
        # ask the user to enter a value
        value = input("Enter a value: ")
        if value == "":
            # if the user presses enter without typing anything, break out of the loop
            break
        # add the value to the list
        list.append(value)
    # print the list
    print("Here's the list:", list)
    # call the function to get the list
get_list()
    
        
    
    
        
    