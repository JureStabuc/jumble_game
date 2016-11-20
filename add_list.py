#Add list of words module, using shelve, possible re-use
import shelve

def list_import():
    #User inputs name
    name = input("\nName: ")
    #When the file name is correct
    while True:
        try:
            #User inputs file name
            filename = input("File name:")
            #Opens the text file and formats it
            with open(filename) as afile:
                the_list = [word.strip(",") for line in afile for word in line.split()]
            #Opens the binary file
            shelf = shelve.open("wordlists.dat")
            #Writes data into binary file
            shelf[name] = the_list
            shelf.sync()
            shelf.close()
            print("\nWord set {} is added.\n".format(name))
            break
        #Catching the error if the file name is incorrect
        except IOError:
            print("\nThe file {} doesn't exist.\n".format(filename))
