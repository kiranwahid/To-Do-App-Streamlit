# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, 
# and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than
# MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and 
# passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH 
# to be 3, but feel free to change it around to test your program.


# Define the function that will be called shorten
def shorten(lst):
    # Define the maximum length of the list
    MAX_LENGTH = 3
    
    # If the length of the list is greater than the maximum length
    while len(lst) > MAX_LENGTH:
        # Remove the last element from the list
        pop_elem = lst.pop()
        # Print the removed element
        print(f"Removed {pop_elem}")
    
    # If the list is shorter than or equal to MAX_LENGTH, leave it unchanged
    print(f"Final list: {lst}")

# Function to get the list from the user
def get_list():
    lst = []
    elem = input("Please enter an element of the list (or press Enter to finish): ")
    
    # Keep asking the user for elements until they press Enter without typing anything
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list (or press Enter to finish): ")
    
    return lst

# Main function to call the other functions
def main():
    # Get the list from the user
    lst = get_list()
    
    # Call the shorten function to trim the list
    shorten(lst)

# Call the main function to run the program
main()
