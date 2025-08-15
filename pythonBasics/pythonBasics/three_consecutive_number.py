# "Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

# Example 1:
# Input: arr = [3,5,4,1]
# Output: false
# Explanation: There are no three consecutive odds.

# Example 2:
# Input: arr = [5,7,34,1,4,9,7,25,12]
# Output: true
# Explanation: [9,7,25] are three consecutive odds."

def myfunc(arr):
    counter = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            counter+=1
            if counter == 3:
                return True
        else:
            counter = 0
    return False

arr1 = [3, 5, 4, 1]
arr2 = [5, 7, 34, 1, 4, 9, 7, 25, 12]
print(myfunc(arr1))
print(myfunc(arr2))
