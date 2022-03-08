import random
from graphics import IMAGES, LOGO
from wordlist import dictionary


def main():
    """
    Main function which contains the whole game code.
    """

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

    # Empty inputs counter
    empty_inputs = 0

    # List of guesses(letters)
    used_letters = []

    # Main logics of the game
    # Displaying logo of the game
    print(LOGO)

    # Introductory messages for the player
    name = input("Enter Your Name:\n").capitalize()
    print("\n")
    print("Welcome to 'Hangman - Fruits & Vegetables'", name)
    print("Try to guess the 4-letter word in less than 6 moves!")
    print("IMPORTANT: You have to use one valid character per turn!")

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
        # and if guess is not an empty input
        if guess in word and guess != "":
            if repeated_inputs == 0:
                print("You've guessed correctly! :)")
            elif guess in used_letters:
                print("This correct answer was used before!")
                wrong_guesses += 1

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
        # If the guess is a repeated input and not in word
        # If the guess is one incorrect letter
        # display the message and decrease number of lives.
        elif guess != used_letters:
            print("\n")
            print("Better luck next time!" " :(")
            # Increase number of incorrect by 1
            wrong_guesses += 1
        else:
            print("\n")
            print("Better luck next time!"" :(")
            wrong_guesses += 1
    
    # END GAME
    # If the user had the max number of incorrect guesses then they've lost,
    #  if not they won.
    if wrong_guesses == max_attempts:
        print(IMAGES[wrong_guesses])
        print("SORRY! YOU'VE LOST! :(")
        print("\n")
        print("The correct word is:", word)
    # If the inputs were repeatedly empty then user loses
    elif empty_inputs > 5:
        max_attempts = 6
        wrong_guesses = 6
        print(IMAGES[wrong_guesses])
        print("SORRY! You've lost due to invalid inputs!")
    elif wrong_guesses > 5:
        max_attempts = 6
        wrong_guesses = 6
        print(IMAGES[wrong_guesses])
        print("SORRY! YOU'VE LOST! :(")
        print("\n")
        print("The correct word is:", word)
    # This is intended for repeated inputs
    else:
        print("\n")
        print("WELL DONE!""\n""You've guessed the correct word: :)", word)

    # RESTART GAME
    # with the possibility of trying again or exiting the game.
    print("\n")
    repeat = input("RESTART GAME: Y/N\n").capitalize()
    if repeat == "Y":
        main()
    elif repeat == "N":
        print("Goodbye!")
        exit()

    # If the user chooses some other letter or symbol
    # this reminds them to use a valid input to restart the game.
    else:
        print("Please input valid character!")
        repeat = input("RESTART GAME: Y/N\n").capitalize()
        if repeat == "Y":
            main()
        else:
            print("Goodbye!")
            exit()


main()
