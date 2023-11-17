import random

class Hangman:
    """ This class is used to create a Hangman game. """
    
    def __init__(self, word_list, num_lives=5):
        """ 
        This initialises the attributes for Hangman.
        
        Parameters: 
        - word_list (list) = A list of words for the Hangman game.
        - num_lives (int) = The number of lives the player begins with. This is set at 5 lives. 
        """
        # Word list set
        self.word_list = word_list
        # Attributes 
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for x in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = [] 

    def check_guess(self, guess):
        """ 
        This checks whether the letter guessed by the player is in the word.

        Parameters: 
        - guess (str) = The letter guessed by the player

        Prints a message to indicate whether the player guessed correctly or incorrectly.
        """
        
        guess = guess.lower()
        # Checks if the letter is in the word
        if guess in self.word:
          print(f"Good guess! '{guess}' is in the word.")
          # Loop through letters to check if letter = guess so "_" is replaced with the guess
          for i, letter in enumerate(self.word):
             if letter == guess:
                self.word_guessed[i] = guess
          # Reduces variable by 1
          self.num_letters -= 1
        else:
          # Reduces lives by 1
          self.num_lives -= 1
          print(f"Sorry, {guess} is not in the word.")
          print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
        """ 
        This asks the player to guess a letter and calls the check_guess method

        Checks if the guessed letter is in the word and checks for input validation to ensure only a single letter is entered
        Using append, guesses are tracked and recorded to the list of guesses
        """
        while True:
            # Asks the user for an input
            guess = input("Guess a letter: ")
            # Checks input is NOT a single alphabetical character
            if not len(guess) == 1 and guess.isalpha():
             print("Invalid letter. Please, enter a single alphabetical character")
            # Checks input is in the list of guesses
            elif guess in self.list_of_guesses:
             print("You already tried that letter!")
            # If input is a single character and not already in list of guesses
            else:
               self.check_guess(guess)
               self.list_of_guesses.append(guess)
               break 
    
# Hangman word list
word_list = ["watermelon", "mango", "pineapple", "strawberry", "blueberry"]
# Testing the code 
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()