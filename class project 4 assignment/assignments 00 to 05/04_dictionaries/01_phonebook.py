# In this program we show an example of using dictionaries to keep track of information in a phonebook.

def read_phonebook():
    phonebook = {}
    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        number = input("Enter a phone number: ")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    for name, number in phonebook.items():
        print(f"{name}: {number}")
        print("---")
        
def search_phonebook(phonebook):
    print("Searching phonebook...")
    name = input("Enter a name: ")
    if name in phonebook:
        print(f"{name}'s phone number is: {phonebook[name]}")
    else:
        print(f"{name} is not in the phonebook")
        
phonebook = read_phonebook()
print_phonebook(phonebook)
search_phonebook(phonebook)
    

