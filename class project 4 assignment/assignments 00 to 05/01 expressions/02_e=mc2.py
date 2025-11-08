# Write a program that continually reads in mass from the user and then outputs the equivalent energy 
# using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2


#  speed of light
c = 299792458

#  take mass from user

mass:float = float(input("Enter a mass: "))

#  calculate energy using formula
# energy = mass * (c**2)
energy = mass * c**2

#  print the result
print(f"\nE = m * C^2")
print(f"\n m = {mass} kg")
print(f"\n C = {c} m/s")
print(f"\nThe equivalent energy of {mass} kg is {energy} Joules.")

