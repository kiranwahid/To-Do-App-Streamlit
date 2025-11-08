# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element
# in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to 
# input the list one element at a time.

#  define function that will be called get_first_element

def get_first_element(lst):
      # Accessing the first element using index 0
    first_element = lst[0]
      # Printing the first element
    print(f"The first element is {first_element}")
    
# Prompt the user to enter the number of elements in the list
n = int(input("Enter a number of element in the list: "))

# Create an empty list to store the elements
lst = []


# Loop through to get user input for each element in the list
for i in range(n):
    elem = input(f"Enter element {i+1}: ")
    lst.append(elem)
 
get_first_element(lst)
    