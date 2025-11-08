# Write a function that takes two numbers and finds the average between the two.

def average(num1:float, num2:float):
    sum = num1 + num2
    return sum / 2

# Test the function
avg1 = average(10, 20)
avg2 = average(10, 30)
final = (avg1 + avg2)

# Print the first average
print(f"first average is {avg1}")

# Print the second average
print(f"second average is {avg2}")

# Print the final average
print(f"final average is {final}")


