# This is a new line string
s = 'First line.\nSecond line.'
print(s)
 
"""
This is a multiline comment
"""
s = """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
print(s)

s = s + " New Text"
print(s)

s = "New " 'Text'
print(s)

s = s + 'Text'

s = "Python" # (012345) (-6 -5 -4 -3 -2 -1)
print(s[0] + " " + s[1])
# print(s[:3])
# print(s[3:])
# print(s[1:4])
print(s[-3:-2])
print(len(s))