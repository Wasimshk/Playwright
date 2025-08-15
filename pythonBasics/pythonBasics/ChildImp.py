
from OopsDemo import Calculator

class ChildImpl(Calculator):
    num2=200
    # def __init__(self):
    #     Calculator.__init__(self, 2, 10)
    #     print("this child class constructor")

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


child_obj = ChildImpl(2, 10)
print(child_obj.getCompleteData())
