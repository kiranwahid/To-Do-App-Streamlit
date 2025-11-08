# Write a function that takes a list of numbers and returns the sum of those numbers.
# The function should be called add_many and should take a list as an argument.

def add_many(numbers) -> int:
    # Initialize a variable to store the sum
    total = 0
# Iterate over each number in the lis
    for number in numbers:
        # Add the numbers to the total
        total += number
        # Return the total sum
    return total

# Test the function with a list of numbers

number:list[int] = [1, 2, 3, 4, 5]
result = add_many(number)
print("sum of all numbers:", result)


