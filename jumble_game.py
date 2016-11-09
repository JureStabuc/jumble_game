import random
from amazement import *
import shelve

#Welcome the player
print("""
    Welcome to Word Jumble.
        Unscramble the letters to make a word.
""")

def wordlist(file):
    with open(file) as afile:
        global the_list
        the_list = [word.strip(",") for line in afile for word in line.split()]

def menu():
    print("1--Play the game")
    print("2--Browse a word set")
    print("3--Add a new word set")
    print("4--Delete a word set")
    print("5--My sorted scores")
    print("6--Exit")
    pick = int(input("Pick one:"))

    if pick == 1:
        game()
    elif pick == 2:
        for i in the_list:
            print(i, end="  ")
    elif pick == 3:
        global name
        name = input("Name: ")
        filename = input("File name:")
        add_list(filename)

def game():
    score = 0
    for i in range(4):
        word = random.choice(the_list)
        theWord = word
        jumble = ""
        while(len(word)>0):
            position = random.randrange(len(word))
            jumble+=word[position]
            word=word[:position]+word[position+1:]
        print("The jumble word is: {}".format(jumble))

        #Getting player's guess
        guess = input("Enter your guess: ").lower()

        #congratulate the player
        if(guess==theWord):
            print("Congratulations! You guessed it")
            score +=1

        else:
            print ("Sorry, wrong guess.")
    print("You got {} out of 10".format(score))

def add_list(file):
    with open(file) as afile:
        the_list = [word.strip(",") for line in afile for word in line.split()]
        print(the_list)
    print ("Shelving Lists ...")
    shelf = shelve.open("wordlists.dat")
    shelf[name]=the_list
    shelf.sync()
    shelf.close()
    print("Success.")
    print("Retrieving word list from shelf")
    shelf = shelve.open("wordlists.dat")
    print("Your words: {}".format(shelf[name]))
    shelf.close()

#filename = "words/amazement_words.txt"
wordlist(filename)
menu()
#game()
