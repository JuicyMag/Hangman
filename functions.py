#this is where our helper functions will live. 
from curses.ascii import *
import random

#letters that are guessed throughout the game - will get added to as users guess
letters_guessed = []

#letters remaining that displays to users so they know what they've tried
letters_remaining = ("a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

#NUMBER OF TURNS - CAN LATER MAKE THIS A VARIABLE USERS SELECT BUT WILL DEFAULT TO CONSTANT
TURNS = 6



#USERS GUESS


 #DONE - returns a random word from the input file 'hangman.wordlist.10000.txt
def pick_random_work(text_file):
    c = open(text_file,'r').read().split()
    return random.choice(c)
    print(random.choice(c))

secret_word = pick_random_work('hangman.wordlist.10000.txt')



#LOGICAL CHECKS
##Need to see if input is valid. Valid = is alphabetical, else throw error
###Need to see if 

while TURNS > 0:
    guess = input("What letter would you like to guess?")    
    if isalpha(guess):
        print("this is a valid guess")

        if guess not in secret_word:
            print("Incorrect Guess. Remaining turns :", TURNS)
            TURNS = TURNS - 1

    else:
        print("this is not a valid guess")
   









#TESTING WORK HERE
# print("Remaining letters are: ")
# print(", ".join(letters_remaining))
