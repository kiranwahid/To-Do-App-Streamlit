# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!)
# and outputs the temperature converted to Celsius.

# The formula for converting Fahrenheit to Celsius is:

# Celsius = (Fahrenheit - 32) * 5 / 9

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9

# Print the converted temperature rounded to two decimal places

print(f"The temperature in Celsius is: {round(celsius, 2)}")
