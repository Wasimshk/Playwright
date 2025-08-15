# Create a Greeting function
# Objective: Create a function that greets the user.
#
# Instructions:
#
# Write a function called GreetUser that takes a single argument username.
#
# The function should print "Hello, [username]! Welcome to the Python course."
#
# Call the function with username "John".
#
# Expected Output:
#
# Hello, John! Welcome to the Python course.


def CalculateAverage(num1, num2, num3):
    return (num1 + num2 + num3) / 3

avgNum = CalculateAverage(10, 20, 30)
print(f"The average of 10, 20, and 30 is {avgNum}")
