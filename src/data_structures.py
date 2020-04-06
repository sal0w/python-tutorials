from collections import deque


a = [3,5]
a[len(a):] = [6,5,3]
# a.remove(3)
print(a.count(3))
a.sort()
sorted(a)

queue = deque()
print(queue)
queue.append(2)
queue.append(3)
print(queue)
print(queue.popleft())
print(queue)

square = list(map(lambda x: x**2,range(10)))
square_for = list(i**j for i in range(10) for j in range(10) if i != j)
# for i in range(10):
#     square.append(i**2)

# print(square_for)

freshfruit = ['passion fruit  ','  banana', '  loganberry ' ]

print(freshfruit)
for fruit in freshfruit:
    print(fruit)
print([fruit for fruit in freshfruit if fruit.strip().startswith("ba")])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([n for num in vec for n in num])

t = 12345, 54321, 'hello!'
s = "dfgdgfg"
# t[1] = 898
# s[2] = str("k")
print(s[2])
t ="tdhtdh"
u = t, (1,2,3,4,6)
print(u)
v = ((1, 2, 3), [3, 2, 1])
# v[0][2] = 4

print(v)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket.add("salow")

print(basket)

a = set('abracadabra')
b = set('alacazam')
print(a-b)

l = [1,2,3]

print(3 in l)

s = "123"

print("3" in s)