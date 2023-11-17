import random

# Task 1: Create the class
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for x in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = [] 

# Task 2: Create methods for running the checks 
    def check_guess(self, guess):
        # Converting guess into lower case
        guess = guess.lower()
        if guess in self.word:
          print(f"Good guess! '{guess}' is in the word.")
          for i, letter in range(len(self.word)):
             if letter == guess:
                self.word_guessed[i] = guess
          self.num_letters -= 1
        else:
          self.num_lives -= 1
          print(f"Sorry, {guess} is not in the word.")
          print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        while True:
            # Ask the user for an input
            guess = input("Guess a letter: ")
            # Check input is NOT a single alphabetical character
            if not len(guess) == 1 and guess.isalpha():
             print("Invalid letter. Please, enter a single alphabetical character")
            # Check input is in the list of guesses
            elif guess in self.list_of_guesses:
             print("You already tried that letter!")
            # If input is a single character and not already in list of guesses
            else:
               self.check_guess(guess)
               self.list_of_guesses.append(guess)
               break 
    
# Task 1 Milestone_2: Define a list of possible words 
word_list = ["watermelon", "mango", "pineapple", "strawberry", "blueberry"]
#  Task 2: Call ask_for_input 
game = Hangman(word_list)
game.ask_for_input()