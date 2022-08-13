#this is where our helper functions will live. 
from curses.ascii import *
from operator import truediv
import random
from tracemalloc import start

#letters that are guessed throughout the game - will get added to as users guess
letters_guessed = []

#letters remaining that displays to users so they know what they've tried
starting_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#NUMBER OF TURNS - CAN LATER MAKE THIS A VARIABLE USERS SELECT BUT WILL DEFAULT TO CONSTANT
TURNS = 6


 #DONE - returns a random word from the input file 'hangman.wordlist.10000.txt
def pick_random_work(text_file):
    c = open(text_file,'r').read().split()
    return random.choice(c)
    print(random.choice(c))


#checks to see if the chars guessed reveal the word. DOES NOT check to see if the entire string input is equal to secret word.
def is_word_guessed(secret_word):
    for char in secret_word:
        if char not in letters_guessed:
            return False
        
    return True 

#i want this function to return the string I'm creating and manipulating with _'s
def guessed_word_sofar(secret_word, letters_guessed):
    guessed_word = ''

    for char in secret_word:
        if char not in letters_guessed:
            guessed_word+='_ '
        else:
            guessed_word += char
    return guessed_word
    

secret_word = pick_random_work('hangman.wordlist.10000.txt')

#LOGICAL CHECKS
##Need to see if input is valid. Valid = is alphabetical, else throw error
###Need to see if letter was already guessed
####Need to check if char was in secret word

print(secret_word)

while True:

    #USERS GUESS
    guess = input("What letter would you like to guess?")   

    if guess.isalpha():
        if guess in letters_guessed:
            print('\n')
            print("You already guessed this, pick another character!")
            print("Letters guessed:",letters_guessed)
            print("Available letters:",starting_letters)
            print('\n')
        else:
            if guess not in secret_word:
                TURNS = TURNS - 1
                letters_guessed.append(guess)
                print("Incorrect Guess. Remaining turns :", TURNS)
                print("Letters guessed:",letters_guessed)
                print("Available letters:",starting_letters)
                print(guessed_word_sofar(secret_word,letters_guessed))
                # print("this is a valid guess")
                # remaining_letters = starting_letters.remove(guess)
                letters_guessed.append(guess)
                starting_letters.remove(guess) 

                
            else:
                letters_guessed.append(guess)
                print(guessed_word_sofar(secret_word,letters_guessed))
                print("Correct guess!Turns remaining:", TURNS)
                print("Letters guessed:",letters_guessed)
    else:
        print("This is not a valid guess. No turn was used.")



    if is_word_guessed(secret_word):
        print("YOU WON! The word was: ", secret_word)
        break

    if TURNS==0:
        print("You ran out of guesses!")
        break
                              