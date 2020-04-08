def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    results = list()
    a, b = 0, 1
    while a < n:
        # print(a,end = ' ')
        results.append(a)
        a, b = b, a+b # a =b
        # b = a+b
    return results

# print(fib(4))
"""
String function string_cat(String* string1,String* string2){
    return "sss";
}
"""
def string_cat(string1,string2):
    string3 = string1+" "+string2
    return string3

# s1 = "Hello"
# s2 = "World"
# s3 = string_cat #Function pointer
# print(s3("H","W"))

# Day 3
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# print(ask_ok("Type something: ",7,"You are typing a wrong value"))
i = 5

def ff(arg=i):
    print(arg)
    return arg
i =6
print(ff())
def f(a, L=None):
    if L is None:
        l = []
    l.append(a)
    return l

# if __name__ == "__main__":
i = 6
print(f(i))
print(f(i))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000,type="UI")

def cheeseshop(*value, **keywords):
    kind = ""
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in value:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("huuhiu",pos ="uhkuhi")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
""" ** - unpacking
voltage = "four million"
state =  "bleedin' demised"
action = "VOOM"
"""
parrot(**d)

def sort_string(pair):
    # print(pair)
    return pair[0] + pair[1]

# Lambda functions
pairs = [[1, 5], [2, 9], [3, 7], [4, 14]]
# pairs.sort(key = sort_string, reverse=True)
pairs.sort(key=lambda a: a[0]+a[1])
print(pairs)
