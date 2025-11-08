# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# Write a function that doubles each element in a list of numbers.

def double_list(numbers):
    # Create a new list to store the doubled numbers
    doubled_numbers = []
    # Iterate over each number in the original list
    for num in numbers:
        # Double the number and add it to the new list
        num_double = num*2
        doubled_numbers.append(num_double)
        # Return the new list
    return doubled_numbers
    # Call the function with the provided list
numbers = [1,2,3,4]
doubled_numbers = double_list(numbers)
print(doubled_numbers)
        

