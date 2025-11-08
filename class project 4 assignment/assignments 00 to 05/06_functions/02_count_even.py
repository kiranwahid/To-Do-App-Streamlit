# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt 
# "Enter an integer or press enter to stop: "),
# and then prints the number of even numbers in the list.
# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def get_even_count(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
    return count  # Return instead of printing

def get_list_of_int():
    lst = []
    while True:
        num = input("Enter an integer or press enter to stop: ")
        if num == "":
            break
        try:
            lst.append(int(num))  # Convert input to int
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return lst

if __name__ == "__main__":
    lst = get_list_of_int()
    even_count = get_even_count(lst)
    print(f"Count of even numbers: {even_count}")  # Print the count outside the function

    