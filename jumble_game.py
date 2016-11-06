import random

#Welcome the player
print("""
    Welcome to Word Jumble.
        Unscramble the letters to make a word.
""")
print("Select an option:")
print("""
1-Play the game""")

def wordlist(file):
    with open(file) as afile:
        global the_list
        the_list = [word.strip(",") for line in afile for word in line.split()]
    print(the_list)

def main():
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
        guess = input("Enter your guess: ")

        #congratulate the player
        if(guess==theWord):
            print("Congratulations! You guessed it")
            score +=1

        else:
            print ("Sorry, wrong guess.")
    print("You got {} out of 10".format(score))

#filename = "words/amazement_words.txt"
#wordlist(filename)
#main()
