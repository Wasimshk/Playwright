
# read the file and store all the lines in a list
# reverse the list
# write the list back to the file

with open("textfile.txt", "r") as readerobj:
    listofLines = readerobj.readlines()
    print(listofLines)
    with open("textfile.txt", "w") as writerobj:
        for line in reversed(listofLines):
            writerobj.write(line)