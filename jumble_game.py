import random
import shelve
import time
import add_list

# Welcome the player
print("""
    Welcome to Word Jumble.
        Unscramble the letters to make a word.
""")

#Main menu function
def menu():
    print("1--Play the game")
    print("2--Browse a word set")
    print("3--Add a new word set")
    print("4--Delete a word set")
    print("5--My sorted scores")
    print("6--Exit")

#Catching exceptions
    while True:
        try:
            pick = int(input("Please select one of the options: "))
        #If the input is not a number
        except ValueError:
            print("\nOops, make sure you input a number.\n")
            return menu()

#When user picks a number the assigned function runs
        if pick == 1:
            game()

        elif pick == 2:
            browse()

        elif pick == 3:
            add_list.list_import()
            return menu()

        elif pick == 4:
            delete()

        elif pick == 5:
            score()

        elif pick == 6:
            print("\nGoodbye!")
            exit()

#Browse a word set function
def browse():
    print("\nRetrieving word sets\n")
    #Open the file with all word sets
    shelf = shelve.open("wordlists.dat")
    #Putting the word sets names into a list
    listname = list(shelf.keys())
    #Making the menu with word sets names and the assigned index number
    for i in listname:
        print("{}--{}".format(listname.index(i)+1,i))
    while True:
        try:
            choice = int(input("\nPlease select: "))
            #Chosing the correct key from user input according to the key's index
            word_set=(listname[choice-1])
            print("\nYour words: \n")
            for i in shelf[word_set]:
                print(i,end=" ")
            print("\n")
            shelf.close()
            return menu()
        #If input is not a number
        except ValueError:
            print("\nOops, make sure you input a number.\n")
        #If list index is out of range
        except IndexError:
            print("\nMake sure you choose the correct file.\n")

def game():
    #Opens the file with all wordsets
    shelf=shelve.open("wordlists.dat")
    listname = list(shelf.keys())
    print("\n")
    #Making the menu with word sets names and the assigned index number
    for i in listname:
        print("{}--{}".format(listname.index(i)+1,i))
    while True:
        try:
            choice = int(input("\nPlease select: "))
            word_set=(listname[choice-1])
            #global wordlist
            wordlist = shelf[word_set]
            score = 0
            #Choosing a random word from the wordlist
            for i in range(10):
                word = random.choice(wordlist)
                theWord = word
                jumble = ""
                #Jumbling the word
                while(len(word) > 0):
                    position = random.randrange(len(word))
                    jumble += word[position]
                    word = word[:position] + word[position + 1:]
                print("\nThe jumble word is: {}".format(jumble))
                # Getting player's guess, formatting input to lower case as words are saved in lower case.
                guess = input("Enter your guess: ").lower()
                # Congratulate the player
                if(guess == theWord):
                    print("Congratulations! You guessed it")
                    score += 1
                else:
                    print("Sorry, wrong guess. The word is {}".format(theWord))
            break
        #If input is not a number
        except ValueError:
            print("\nOops, make sure you input a number.\n")
        #If list index is out of range
        except IndexError:
            print("\nMake sure you choose the correct file.\n")

    #Printing the score
    print("\nYou got {} out of 10\n".format(score))
    #Recording the score
    shelf = shelve.open("score.dat")
    score_a = str(score)
    shelf[score_a]=[time.ctime()]
    shelf.sync()
    shelf.close()
    return menu()

#Displaying user's scores
def score():
    #Format for score display
    print("\n")
    myformat = "{:10s} {:10s}"
    print(myformat.format('Score', 'Date'))
    print("-"*35)
    #Opens the file with recorder scores
    shelf = shelve.open("score.dat")
    #Puts the scores into a list
    listname = list(shelf.keys())
    #Sorts the keys-scores
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
    print("\n")
    return menu()

def delete():
    #Opens the word sets file
    shelf=shelve.open("wordlists.dat")
    listname = list(shelf.keys())
    print("\nSelect the word set you want to delete")
    #Prints all files available for deleting
    for i in listname:
        print("{}--{}".format(listname.index(i)+1,i))
    while True:
        try:
            #User chooses a file
            choice = int(input("Please select: "))
            word_set=(listname[choice-1])
            #File gets deleted
            del shelf[word_set]
            shelf.sync()
            shelf.close()
            print("\nWord set {} deleted!\n".format(word_set))
            return menu()
        #If input is not a number
        except ValueError:
            print("\nOops, make sure you input a number.\n")
        #If list index is out of range
        except IndexError:
            print("\nMake sure you choose the correct file.\n")
menu()
