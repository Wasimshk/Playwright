#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100  #class variables
    #default constructor

    def __init__(self, a, b):
        # in order to use a and b parameters through out the class in any class method we will need to assign the parameter to class object(i.e self)
        # if we do not assign then the parameters will only available inside the constructor
        # self.a, self.b will be instance variables
        self.a = a
        self.b = b
        print("I am called automatically when object is created")
        # print(a, b)

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.a + self.b + Calculator.num


obj = Calculator(2, 3)
obj.getData()
# print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
# print(obj1.Summation())



