import random

# Choosing a random word from the list
def random_word(word_list):
    return random.choice(word_list)

# Task 3: Create functions to run the checks 
def check_guess(word, guess):
    # Converting guess into lower case
    guess = guess.lower()
    # Task 2: Check whether the guess is in the word
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Task 3: Create functions to run the checks 

def ask_for_input():
    # Task 1: Continuously ask user for a letter and validate it
    while True: 
        # Ask the user for an input
         guess = input("Guess a letter: ")
        # Check input is a single alphabetical character
         if len(guess) == 1 and guess.isalpha():
        # If guess passes check, break out of loop
             check_guess(word, guess) 
             break 
         else:
        # If guess is invalid, print message
             print("Invalid letter. Please, enter a single alphabetical character.")


# Task 1 Milestone_2: Define a list of possible words 
word_list = ["watermelon", "mango", "pineapple", "strawberry", "blueberry"]

# Task 2 Milestone_2: Choose a random word from the list 
word = random_word(word_list)

# Task 3: Call ask_for_input 
ask_for_input()
