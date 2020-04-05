# List

l = [0,1,2,3]
print(l)
l = ["0",1,"4"]
print(l)
l.reverse()
print(l)
# Iterator
for i in l: # Interates values
    print(i)

for i in range(len(l)): # 0 1 2 for(i=0,i<len(l),i++)
    print(l[i])

l =[]
print(l)

# Exercises 1
"""
Append a value in list
create variable a -> is a empty list
append values 
"""
a = []
#opentions
a.append(8)
print(a)
# Exercise 2
"""
Var: l = ["1",2,"3",4,"5"]
Q1: I want to print only the numbers
"""
l = ["1",2,"3",4,"5"]
for num in l:
    if type(num) == int:
        print(num)

# 2 dimentional
# a = [["0","1","2"],#inner 0
#     ["1"]#inner 1
#     ] #outster 0 , 1 
# print(a[0][0])

# x = str(input("Please enter an integer: "))
# print("The user input is "+x)

devices = ["Mouse","Keyboard","Laptop"]
devices.insert(1,"printer")

for device in devices:
    print(device)

word = "Python"

for i,w in enumerate(word,1):
    print(str(i) +" word is "+w)

numbers = list(range(10)) #[]
numbres20 = list(range(10,20))
numbers.extend(numbres20)

#Excersise 3
"""
we have a list called numbers
find whether a number is in that list
"""
print(numbers)
number = "10"
if number.isdigit():
    if int(number) in numbers:
        print(str(number)+" is present")
    else:
        print(str(number)+" is not present")
else:
    print("Number is of type String")

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a odd number", num)

def function():
    pass