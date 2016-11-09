shelf=shelve.open(#filename)
for key in shelf.keys():
    print(key, ": \n"m shelf[key], "\n \n")


delete_key=input("Do you want to delete")
if delete_key==key in shelf.keys():
    del shelf[key]
    for key in shelf.keys():
        print(key, ": \n"m shelf[key], "\n \n")
