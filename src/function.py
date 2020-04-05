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

print(fib(4))
"""
String function string_cat(String* string1,String* string2){
    return "sss";
}
"""
def string_cat(string1,string2):
    string3 = string1+" "+string2
    return string3

s1 = "Hello"
s2 = "World"
s3 = string_cat #Function pointer
print(s3("H","W"))
