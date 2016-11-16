import random
import shelve
import time

# Welcome the player
print("""
    Welcome to Word Jumble.
        Unscramble the letters to make a word.
""")


#Main menu
def menu():
    print("1--Play the game")
    print("2--Browse a word set")
    print("3--Add a new word set")
    print("4--Delete a word set")
    print("5--My sorted scores")
    print("6--Exit")
    pick = int(input("Please select: "))

#When user picks a number the assigned function runs
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

#Browse a wordlist function
def browse():
    print("Retrieving word list from shelf")
    #Open the wordlist
    shelf = shelve.open("wordlists.dat")
    #Putting the keys into a list
    listname = list(shelf.keys())
    #Making the menu with keys and the assigned index number
    for i in listname:
        print("{}--{}".format(listname.index(i)+1,i))
    choice = int(input("Please select: "))
    #Chosing the correct key from user input according to the key's index
    word_set=(listname[choice-1])
    print("Your words:")
    for i in shelf[word_set]:
        print("{}".format(i))
    shelf.close()
    return menu()

    #the_list = [word.strip(",") for line in afile for word in line.split()]

def game():
    shelf=shelve.open("wordlists.dat")
    listname = list(shelf.keys())
    for i in listname:
        print("{}--{}".format(listname.index(i)+1,i))
    choice = int(input("Please select: "))
    word_set=(listname[choice-1])
    global wordlist
    wordlist = shelf[word_set]
    score = 0
    #Choosing a random word from the wordlist
    for i in range(4):
        word = random.choice(wordlist)
        theWord = word
        jumble = ""
        #Jumbling the word
        while(len(word) > 0):
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[position + 1:]
        print("The jumble word is: {}".format(jumble))
        # Getting player's guess
        guess = input("Enter your guess: ").lower()
        # Congratulate the player
        if(guess == theWord):
            print("Congratulations! You guessed it")
            score += 1
        else:
            print("Sorry, wrong guess. The word is {}".format(theWord))
    #Printing the score
    print("You got {} out of 10".format(score))
    #Recording the score
    shelf = shelve.open("score.dat")
    score_a = str(score)
    shelf[score_a]=[time.ctime()]
    shelf.sync()
    shelf.close()
    return menu()
#Displaying user's scores
def score():
    myformat = "{:10s} {:13s}"
    print(myformat.format('Score', 'Date'))
    print("-"*26)
    shelf = shelve.open("score.dat")
    listname = list(shelf.keys())
    for num in range(len(listname)-1,0,-1):
        for i in range(num):
            if listname[i]<listname[i+1]:
                temp = listname[i+1]
                listname[i+1] = listname[i]
                listname[i] = temp
    for key in listname:
        dates = shelf[key]
        for val in dates:
            print(myformat.format(key, val))
    shelf.close
    return menu()
#Adding a wordset
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
    choice = int(input("Please select: "))
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
