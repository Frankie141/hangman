# easy random work generator
import random
from words import words

words = ['Python', 'JavaScript', 'Computer', 'player',
         'library', 'Peacock', 'Rainbow', 'Rock', 'Paper']

# Welcome message and name input
name = input("Please enter your name: ")
print(""" 
        Welcome name to Hangman. You will be playing against the computer.
        The computer will randomly choose a word and you will need to choose 
        letters to figure out the word. You will have 10 guesses to pick your 
        letters. Good luck name\n
    """)

def get_random_word(words):
    word = random_word.choice(words) # Chooses random word from the list
    while '-' in word or ' ' word: 
    word = random_word.choice(words)

    return word    