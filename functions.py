#this is where our helper functions will live. 
import random

# a = open('hangman.wordlist.10000.txt','r')
# b = a.read()
# c = b.split()
# print(random.choice(c))

#DONE - returns a random word from the input file 'hangman.wordlist.10000.txt
def pick_random_work(text_file):
   c = open(text_file,'r').read().split()
   return random.choice(c)
   print(random.choice(c))



