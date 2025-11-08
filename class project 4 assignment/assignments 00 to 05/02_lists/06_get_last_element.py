# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element
# in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


# #  define function that will be called get_last_element
def get_last_element(lst):
    # Accessing the last element using index -1
    last_element  = lst[-1]
    # Printing the last element
    print(f"The last element is {last_element}")
    

# Prompt the user to enter the number of elements in the list of numbers
n = int(input("Enter a number of elements in the list: "))
 
#  create an empty list to store the numbers

lst = []

# Prompt the user to enter each number in the list
for i in range(n):
    num = input(f"Enter element {i+1}: ")
    lst.append(num)

# Call the function to get the last element
get_last_element(lst)