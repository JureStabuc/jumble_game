#Add list of words module, using shelve, possible re-use.
import shelve

def list_import():
    #User inputs name
    name = input("Name: ")
    #User inputs filename
    filename = input("File name:")
    #Opens the text file and formats it
    with open(filename) as afile:
        the_list = [word.strip(",") for line in afile for word in line.split()]
    print("Shelving Lists ...")
    #Opens the binary file
    shelf = shelve.open("wordlists.dat")
    #Writes data into binary file
    shelf[name] = the_list
    shelf.sync()
    shelf.close()
    print("Success.")
