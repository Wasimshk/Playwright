# Understanding class creation in Python
# Objective: Create a basic calculator class to perform addition, subtraction, multiplication, and division.
#
# Instructions:
#
# Create a class named BasicCalculator.
#
# Define a constructor that initializes two numbers. Use numbers 10 & 5
#
# Implement methods for:
#
# Addition
#
# Subtraction
#
# Multiplication
#
# Division
#
# Each method should return the result of the operation.
#
# Create an instance of the BasicCalculator class and demonstrate the functionality of each method.
#
# Example Output:
#
# Addition: 10 + 5 = 15
# Subtraction: 10 - 5 = 5
# Multiplication: 10 * 5 = 50
# Division: 10 / 5 = 2.0



class BasicCalculator:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def addition(self):
        return self.number1 + self.number2

    def subtraction(self):
        return self.number1 - self.number2

    def multiplication(self):
        return self.number1 * self.number2

    def division(self):
        return self.number1 / self.number2


# # Example usage (optional):
operation = BasicCalculator(10, 5)
print("Addition:", operation.addition())
print("Subtraction:", operation.subtraction())
print("Multiplication:", operation.multiplication())
print("Division:", operation.division())

