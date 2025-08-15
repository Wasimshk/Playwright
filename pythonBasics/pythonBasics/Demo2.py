
values = [1, 2, "rahul", 4, 5]
# List is data type that allows multiple values and can be different data types

print(values[0])  # 1

print(values[3])  # 4
print(values[-1])  #5
print(values[1:3])  # 2 rahul
values.insert(3, "shetty")   #[1, 2, 'rahul', 'shetty', 4, 5]
print(values)
values.append("End")  #[1, 2, 'rahul', 'shetty', 4, 5, 'End']
print(values)

values[2] = "RAHUL" #Updating

del values[0]

print(values)

# Tuple - Same as LIST Data type but immutable
val = (1, 2, "rahul", 4.5)

print(val[1])

#val[2] = "RAHUL"

print(val)

# Dictionary
dic = {"a": 2, 4:"bcd", "c": "Hello world"}

print(dic[4])
print(dic["c"])

#
dict = {}

dict["firstname"] = "Rahul"

dict["lastname"] = "shetty"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])


Values = [1, 2, 3.2, 5.5, "wasim"]
print(Values)
Values.insert(5,"Shaikh")
print(Values)
values.append("appended value")
print(Values)
Values[4] = "almas"
print(Values)
del Values[0]
print(Values)

val2 = (1, 2, 3.2, 5.5, "wasim")


# dictionary
dict1 = {"name": "wasim", "age":30, 7:"number"}
print(dict1)
print(dict1["name"])
print(dict1[7])

emptyDict = {}
print(emptyDict)
emptyDict["firstname"] ="Wasim"
emptyDict["lastname"] = "shaikh"
emptyDict["age"] = 29
emptyDict[7] = "number"

print(emptyDict)

# Loop
# print sum of first 5 natural number
sum1 = 0
for i in range(1, 6):
    sum1 = sum1 + i
print(sum1)

# print every 2nd value from 1 - 20
for i in range(1, 21, 2):
    print(i)








