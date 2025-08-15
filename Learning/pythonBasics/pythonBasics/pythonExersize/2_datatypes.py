# Variable Assignment and Types
# Create three variables: age, height, and favorite_color. Assign them values 25, 5.9, blue:
#
# age: an integer (e.g., 25)
#
# height: a float (e.g., 5.9)
#
# favorite_color: a string (e.g., "blue")
#
# Use the print function to display each variable and its type using the type() function.
#
# Expected Result:
#
#
#
# Age: 25 | Type: <class 'int'>
# Height: 5.9 | Type: <class 'float'>
# Favorite Color: blue | Type: <class 'str'>

age = 25
height = 5.9
favorite_color = "blue"

print("Age: " + str(age) + " | Type: " + str(type(age)))
print("Height: " + str(height) + " | Type: " + str(type(height)))
print("Favorite Color: " + str(favorite_color) + " | Type: " + str(type(favorite_color)))

# dict = {"Age":25, "Height":5.9, "favorite_color":"blue"}

# for value in dict:
#     print(value + ": " + str(dict[value]) + " | " + str(type(dict[value])))