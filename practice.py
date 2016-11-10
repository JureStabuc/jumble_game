import shelve
shelf=shelve.open("wordlists.dat")
listname = list(shelf.keys())
for i in listname:
    print("{}--{}".format(listname.index(i),i))
word_set = int(input("Pick one:"))
print(listname[word_set])
