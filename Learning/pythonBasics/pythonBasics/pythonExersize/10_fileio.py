# Count Lines in a File
# Objective: Count and print the number of lines in a file.
#
# Instructions:
#
# Use the attached text file "file1.txt"
#
# Write a Python script that opens the file, reads through it line by line, counts how many lines it has, and prints the total count.
#
# Expected result:
#
# Total number of lines: 5
from itertools import count

# with open("file1.txt", "r") as reader:
#     lines = reader.readlines()
#     counter = 0
#     for line in lines:
#         # print(line)
#         counter = counter + 1
#     print("Total number of lines:", counter)


with open("file1.txt", "r") as reader1:
    lines = reader1.readlines()
    counter = 0
    for line in lines:
        print(line, end="")
        counter+=1
    print("\nnumber of lines: ", counter)