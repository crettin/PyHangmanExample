# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def is_alive():
    return lives != 0


def is_victorious():
    # Iterate through all letters in word to make sure it's in there
    for i in word:
        if not guessedLetters.find(i) != -1:
            return 0

    return 1


def is_letter_already_guessed(checked_guess):
    for i in guessedLetters:
        if checked_guess == i:
            return 1
    return 0


def is_guess_valid(checked_guess):
    return checked_guess.isalpha() and len(checked_guess) == 1


def take_guess():
    entered_guess = input("Pick a letter: ")

    if not is_guess_valid(entered_guess):
        print("Must be a single a-z character, idiot! \n")
        entered_guess = take_guess()

    if is_letter_already_guessed(entered_guess):
        print("Already tried this mate! \n")
        entered_guess = take_guess()

    return entered_guess.lower()


def is_guess_correct(checked_guess):
    return word.find(checked_guess) != -1


def assign_random_word():
    # Pick a random word from the list then assign it to the global word variable
    word_int = random.randint(0, len(POSSIBLE_WORDS) - 1)
    global word
    word = POSSIBLE_WORDS[word_int]


def generate_revealed_letters_string():
    # build a string representing the letters found and not found in the word then return it
    built_string = ""
    for i in word:
        if guessedLetters.find(i) != -1:
            built_string += " " + i + " ";
        else:
            built_string += " _ "
    return built_string


def generate_guess_letters_string():
    # build a string representing the letters found and not found in the word then return it
    built_string = ""
    for i in guessedLetters:
        built_string += " " + i + " "
    return built_string


def print_game_state():
    print("-----------------------------")
    print("Revealed Letters: {}".format(generate_revealed_letters_string()))
    print("-----------------------------")
    print("Guessed Letters: {}".format(generate_guess_letters_string()))
    print("-----------------------------")
    print("Lives remaining: {} \n".format(lives))


def initiate_game_data():
    assign_random_word()
    global guessedLetters
    global lives
    lives = STARTING_LIVES
    guessedLetters = ""


def play_game():
    initiate_game_data()

    while is_alive() and not is_victorious():
        # Print the current game states
        print_game_state()

        # Take input from player, validate it then apply necessary logic
        guess = take_guess()

        # Check if the guess was correct
        if is_guess_correct(guess):
            print("Your guess " + guess + " was correct! \n")
        else:
            print("Guess " + guess + " was incorrectly you loose a life! \n")
            global lives
            lives -= 1
        global guessedLetters
        guessedLetters += guess

    if is_alive():
        print("you win mate! word was: {} \n".format(word))
    else:
        print("you're shit mate! word was {} \n".format(word))


def is_playing():
    play_again_pick = input("Play again? (Y/N): ")
    print("\n")
    if not play_again_pick.lower().startswith("y"):
        return 0
    return 1


STARTING_LIVES = 5
POSSIBLE_WORDS = ["treat", "hello", "goodbye", "passport", "vehicle", "dog"]

word = ""
guessedLetters = ""
lives = 0

play_game()

# Constantly attempt to replay the game until player types something other than y
while is_playing():
    play_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
