# "Check if a String Contains Only Unique Characters

# Input = ""abcdef"" # Output: True
# Input = ""hello""  # Output: False"

mylist = []
str = input("Enter a string: ")
length = len(str)

for i in range(length):
    mylist.append(str[i])
myset = set(mylist)

print("True" if len(myset) == length else "False")