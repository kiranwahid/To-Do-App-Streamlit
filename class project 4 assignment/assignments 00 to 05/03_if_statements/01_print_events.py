# Write a program that prints the first 20 even numbers. There are several correct approaches, 
# but they all use a loop of some sort. Do no write twenty print statements
# The first even number is 0:
# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38


def main():
    for i in range(20):
        print(i * 2)
        # Alternative solution using list comprehension:
        # print([i * 2 for i in range(20)])
        # Another alternative solution using the built-in map function:
        # print(list(map(lambda x: x * 2, range(20))))
        # Another alternative solution using the built-in filter function:
        # print(list(filter(lambda x: x % 2 == 0, range(41))))  # This will print the first 21 even numbers
      
if __name__ == "__main__":
    main()