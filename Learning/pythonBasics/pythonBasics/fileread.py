fileObj = open("textfile.txt")
# read all contents
# print(fileObj.read())
# read specific number of characters
# print(fileObj.read(10))

# note: if one read() already completed reading and reached eof then the 2nd read wont read anything, and first read completes reading a few characters then the next read() will continue reading after the last read character

# read single line at a time
# read complete single line
# print(fileObj.readline())
# read specific number of characters in a single line
# print(fileObj.readline(4))


# print all the contents line by line
# line = fileObj.readline()
# while line!="":
#     print(line)
#     line = fileObj.readline()

listoflines = fileObj.readlines()
print(listoflines)
for line in listoflines:
    print(line)

fileObj.close()