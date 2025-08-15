arr = [1, 2 , 3, 5, 8, 1, 9, 6]
largest = seclargest = 0
for number in arr:
    if number > largest:
        seclargest = largest
        largest = number
    elif number > seclargest and seclargest != largest:
        seclargest = number

print(largest)
print(seclargest)