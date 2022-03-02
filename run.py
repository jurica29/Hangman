# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from graphics import IMAGES, LOGO
from wordlist import dictionary


    def fetch_word():
        """
        Function for fetching random word from the list of words.
        """
        return random.choice(dictionary)

    # Variables for the game
    # Fetching a random word from the list of words
    word = fetch_word()

    # Variable for the end game
    # related to the number of images used for the game art
    max_attempts = len(IMAGES) - 1

    # Blanks for each letter in a word
    current_guess = "-" * len(word)

    # Wrong guess counter
    wrong_guesses = 0

    # Number of invalid inputs
    attempts = 0

    # List of guesses(letters)
    used_letters = []

    # Main logics of the game
    # Displaying logo of the game
    print(LOGO)

    # Introductory messages for the player
    name = input("Enter Your Name:\n").capitalize()
    print("\n")
    print("Welcome to 'Hangman - Fruits & Vegetables'", name)
    print("Try to guess the word in less than 6 moves!")