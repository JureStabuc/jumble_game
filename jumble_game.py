import random
import shelve

# Welcome the player
print("""
    Welcome to Word Jumble.
        Unscramble the letters to make a word.
""")

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
        browse()

    elif pick == 3:
        global name
        name = input("Name: ")
        filename = input("File name:")
        add_list(filename)

    elif pick == 4:
        delete()

    elif pick == 5:
        score()

def browse():
    print("Retrieving word list from shelf")
    shelf = shelve.open("wordlists.dat")
    listname = list(shelf.keys())
    for i in listname:
        print("{}--{}".format(listname.index(i)+1,i))
    choice = int(input("Pick one:"))
    word_set=(listname[choice-1])
    print("Your words: {}".format(shelf[word_set]))
    shelf.close()
    return menu()

def game():
    shelf=shelve.open("wordlists.dat")
    listname = list(shelf.keys())
    for i in listname:
        print("{}--{}".format(listname.index(i)+1,i))
    choice = int(input("Pick one:"))
    word_set=(listname[choice-1])
    global wordlist
    wordlist = shelf[word_set]
    score = 0
    for i in range(4):
        word = random.choice(wordlist)
        theWord = word
        jumble = ""
        while(len(word) > 0):
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[position + 1:]
        print("The jumble word is: {}".format(jumble))

        # Getting player's guess
        guess = input("Enter your guess: ").lower()

        # congratulate the player
        if(guess == theWord):
            print("Congratulations! You guessed it")
            score += 1

        else:
            print("Sorry, wrong guess.")
    print("You got {} out of 10".format(score))
    shelf = shelve.open("score.dat")
    shelf["score"]=[score]
    shelf.sync()
    shelf.close()
    return menu()

def score():
    shelf = shelve.open("score.dat")
    for key in shelf.keys():
        print(shelf[key])
    shelf.close()
    return menu()

def add_list(file):
    with open(file) as afile:
        the_list = [word.strip(",") for line in afile for word in line.split()]
    print("Shelving Lists ...")
    shelf = shelve.open("wordlists.dat")
    shelf[name] = the_list
    shelf.sync()
    shelf.close()
    print("Success.")
    return menu()

def delete():
    shelf=shelve.open("wordlists.dat")
    listname = list(shelf.keys())
    for i in listname:
        print("{}--{}".format(listname.index(i)+1,i))
    choice = int(input("Pick one:"))
    word_set=(listname[choice-1])
    #if word_set == i in listname.keys():
    del shelf[word_set]
    shelf.sync()
    shelf.close()
    #else:
        #print("ERROR")
        #return delete()
    return menu()
menu()
