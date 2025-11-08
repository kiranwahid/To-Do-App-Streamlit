import math

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs
# the length of the third side (the hypotenuse) using the Pythagorean theorem!

#      |
#      |\
#      | \
#  AC  |  \ BC (Hypotenuse)
#      |   \
#      |____\
#       AB


#  get the input from the user

ab = float(input("Enter a length of AB: "))
ac = float(input("Enter a length of AC: "))

# Mathematically, it looks like this:
# BC2 = AB2 +AC2

#  calculate the length of BC using the Pythagorean theorem

bc = math.sqrt(ab**2  + ac**2)

#  print the result

print(f"The length of BC (the hypotenuse) is: {bc}")
