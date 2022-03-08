import random
import string
from words import words

# Welcome message and name input
name = input("Please enter your name: ")
print(""" 
        Welcome name to Hangman. You will be playing against the computer.
        The computer will randomly choose a word and you will need to choose 
        letters to figure out the word. You will have 10 guesses to pick your 
        letters. Good luck name\n
    """)


def get_random_word(words):
    #Chooses random word from the list
    word = random_word.choice(words)

    return word.upper()


def play_game(word):
    word_execution = "_" * len(word)
    guessed = False
    letters_guessed = []
    words_guessed = []
    attempts = 7

    get_random_word(words)

    print()
    print('The word contains', len(word), 'letters.')
    print(len(word) * '_')

    while guessed == False and attempts > 0:
        print('You have ' + str(attempts) + ' attempts')
        guess = input('Take a guess for the missing letter or word.').lower()