#this is where our helper functions will live. 
from curses.ascii import *
import random
from tracemalloc import start

#letters that are guessed throughout the game - will get added to as users guess
letters_guessed = []

#letters remaining that displays to users so they know what they've tried
starting_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

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

while TURNS > 1:
    guess = input("What letter would you like to guess?")    
    if isalpha(guess):
        if guess in letters_guessed:
            print('\n')
            print("You already guessed this, pick another character!")
            print("Letters guessed:",letters_guessed)
            print("Available letters:",starting_letters)
            print('\n')
        else:
            if guess not in secret_word:
                print("Incorrect Guess. Remaining turns :", TURNS)
                # print("this is a valid guess")
                # remaining_letters = starting_letters.remove(guess)
                letters_guessed.append(guess)
                TURNS = TURNS - 1
                starting_letters.remove(guess) 

                print('\n')
                print("Incorrect guess! Turns remaining:", TURNS)
                print("Letters guessed:",letters_guessed)
                print("Available letters:",starting_letters)
                print('\n')
            
            else:
                letters_guessed.append(guess)
                print("Correct guess!Turns remaining:", TURNS)
                print("Letters guessed:",letters_guessed)
                
                
                
    else:
        print("This is not a valid guess. You didn't have a turn used.")
print("Game over!")










#TESTING WORK HERE
# print("Remaining letters are: ")
# print(", ".join(letters_remaining))
