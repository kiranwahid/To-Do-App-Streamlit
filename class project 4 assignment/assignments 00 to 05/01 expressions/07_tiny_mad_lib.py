# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun 
# sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually 
# filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of
# a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.
# You need to fill in the blanks to complete the sentence and print it to the user.

print("\nWelcome to the MadLib Game!")

print("\nPlease provide the following words to complete the story:")


# Prompt the user for a name

name = input("Enter a name: ")

# Prompt the user for an adjective

adjective1 = input("Enter an adjective: ")


# Prompt the user for a animal

animal = input("Enter an animal: ")

# Prompt the user for a verb

verb = input("Enter a verb: ")

# Prompt the user for  another an adjective

adjective2 = input("Enter another an adjective: ")

# Prompt the user for a food

food = input("Enter a food: ")

place = input("Enter a place: ")

# Create the MadLib story
story = f"One day, {name} was walking through the {adjective1} forest when they encountered a {adjective2} {animal}. Without hesitating, {name} decided to {verb} and offer the {animal} some {food}. Surprisingly, the {animal} accepted the food and they both became best friends, traveling together to {place}."


# complete story with user input

print("\nHere's your Mad Lib story:")

print(story)