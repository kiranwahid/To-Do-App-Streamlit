# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.


def get_age():
     Anton =  21
     Beth = Anton + 6
     Chen = Beth + 20
     Drew = Chen + Anton
     Ethan = Chen
     
     print(f"Anton is {Anton} years old.")
     print(f"Beth is {Beth} years old.")
     print(f"Chen is {Chen} years old.")
     print(f"Drew is {Drew} years old.")
     print(f"Ethan is {Ethan} years old.")
     
     
 
get_age()


    