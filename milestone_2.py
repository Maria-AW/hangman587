import random

def random_word(word_list):
    return random.choice(word_list)
 
# Task 1: Define a list of possible words 
word_list = ["watermelon", "mango", "pineapple", "strawberry", "blueberry"]

# Task 2: Choose a random word from the list 
word = random_word(word_list)

# Task 3: Ask the user for an input
guess = input("Enter a single letter: ")

# Task 4: Check that the input is a single character
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else: 
    print("Oops! That is not a valid input.")

