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

    # Repeated inputs counter
    repeated_inputs = 0

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

    # GAME LOOP
    # Main loop starting with a compound statement
    while wrong_guesses < max_attempts and current_guess != word:
        print(IMAGES[wrong_guesses])
        print("So far, the word is: ", current_guess)
        guess = input("Enter your character guess:\n")
    # Converting user guess to uppercase letter
        guess = guess.upper()

        # Check if letter was already used and
        # if there was no empty input
        # decrease lives if it was
        if guess in used_letters and len(guess) == 1:
            wrong_guesses += 1
            repeated_inputs += 1
            empty_inputs += 1
            print("WARNING! You've already tried that!")
            print("\n")
            guess = guess.upper()
        # Add new guessed letter to list of guessed letters
        used_letters.append(guess)

        # Check if guessed letter is located in the given secret word
        # and if guess is empty input
        if guess in word and guess != "":
            if repeated_inputs < 1:
                print("\n")
                print("You've guessed correctly! :)")

            # Give a new version of the word with mixed letters and dashes
            new_current_guess = ""
        # Checking every letter inside the word
        # if the guessed letter is equal the the one in word
        # then swap it with the actual letter.
            for letter in range(len(word)):
                if guess == word[letter]:
                    new_current_guess += guess
                else:
                    new_current_guess += current_guess[letter]
        # Reassigning current guess to be a new version
            current_guess = new_current_guess
        # If the guess is longer than one letter or not a letter
        # Display the warning message and decrease lives
        elif len(guess) != 1:
            print("WARNING! You need to use one character per turn!")
            wrong_guesses += 1
            empty_inputs += 1
        # If the guess is not a letter, then display the warning message
        # increase wrong guesses
        elif guess.isalpha() is False:
            wrong_guesses += 1
            print("WARNING! You must use one valid character per turn!")