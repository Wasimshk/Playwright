# def mergeList(l1, l2):
#     return sorted(set(l1+l2))
list1 = [0, 1, 3, 5, 7, 9, 10, 0, 0, 12, 1]
list2 = [2, 4, 6, 8, 10, 12, 0]
#
# print(mergeList(list1, list2))

def mergelists(l1, l2):
    return sorted(set(l1 + l2))

# print(mergelists(list1, list2))


set1 = set(list1)
set2 = {2, 4, 6, 8, 10, 12, 0, 15}

# Union of set1 and set2 → all items from both sets
print(set1 | set2)
# Intersection → items present in both sets
print(set1 & set2)
# Difference → items in set1 but not in set2
print(set1 - set2)
# Symmetric difference → items in either set1 or set2, but not in both
print(set1 ^ set2)