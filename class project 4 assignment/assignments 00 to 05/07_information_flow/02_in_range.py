# Implement the following function which takes in 3 integers as parameters:
# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be
# greater than low. """

def in_range(n, low, high):
    if n <= low or n >= high:
        return False
    else:
        return True

print(in_range(2, 1, 3))  # True
print(in_range(1, 1, 3))  # false
print(in_range(0, 1, 3))  # False