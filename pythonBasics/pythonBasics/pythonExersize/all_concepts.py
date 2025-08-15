# # //////////////////////////////////////
# # merge lists + remove duplicate value + sort
# def mergelists(l1, l2):
#     return sorted(set(l1+l2))
#
# list1 = [0, 1, 3, 5, 7, 9, 10]
# list2 = [2, 4, 6, 8, 10, 12, 0]
# print(mergelists(list1, list2))
#
# # /////////////////////////////////////
# # print pattern
# for i in range(1, 10):
#     for j in range(i):
#         print("*", end=" ")
#     print("")
#
# # ////////////////////////////////////
# # ternary operator / even odd
# print("add number to see if its even or odd: ")
# number=int(input())
# print("even" if number%2==0 else "odd")

# ////////////////////////////////////
# list comprehension
# print first letter of each words in list
mylist = ["Wasim", "Sarfuddin", "Shaikh"]
# normal for loop
l = []
for word in mylist:
    l.append(word[0])
print(l)
# list comprehension
print([word[0] for word in mylist])
# reverse each word and store it to list
mylist2 = list(input().split())
# for loop basic without list
for word in mylist2:
    print(word[::-1], end=" ")
# for loop in list
reverseList = []
for word in mylist2:
    reverseList.append(word[::-1])
print(reverseList)
# list comprehension
print([word[::-1] for word in mylist2])

# set
