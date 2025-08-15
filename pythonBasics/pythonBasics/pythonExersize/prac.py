
class Wasim:
    a = 10
    b = 20

    def addition(self, num1, num2):
        return num1 + num2 + self.a + Wasim.b


obj1 = Wasim()
print(obj1.a)
print(obj1.addition(1,2))


# 2nd largest
list1 = [2, 4, 6, 8, 10, 12, 0, 15, 14]

large = secLarge = 0
for i in list1:
    if i > large:
        secLarge = large
        large = i
    elif i>secLarge and i != large:
        secLarge = i

print("largest: ", large)
print("SecLargest: ", secLarge)