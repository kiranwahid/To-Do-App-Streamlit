# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. 
# Foot is the singular, and feet is the plural.



# inches per foot

inches_per_foot = 12

def feet():
    # get feet from user
    feet = float(input("Enter a number of feet: "))
    inches = feet * inches_per_foot
    return (f"That is {inches} inches")


get_result = feet()   

print(get_result) 