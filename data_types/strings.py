
str
long_string = '''
WOW
0 0
---
'''  # three single quotes will make multiline string
# string concatination print('hello' + 'Dan')
# Type conversion
a = str(100)  # string
b = int(a)  # int
c = type(b)
print(c)

# escape sequence whatever comes directly after \ is treated as a string, to use \ in the string use \\
# \t adds a tab, \n is a newline

# formatted strings
name = 'Johnny'
age = 55
print('hi' + name + '. You are ' + str(age) + ' years old')
# ORRRRRR use formatted string
print(f'hi {name}. You are {age} years old')
# Using Python 2 ther is no f in front to format
print('hi {1}. You are {0} years old'.format(name, age))

# String indexes
str = '01234567'
print(str[0])  # will print 0
print(str[0:8])  # will print 01234567
# Now using a "stepover"
print(str[0:8:2])  # will print 0246
# In Python the - negative index starts from the end
print(str[-1])  # will print 7, -2 will print 6
print(str[::-1])  # will print 76543210

# this is called SLICING
# str[start:stop:stepover]
# strings are immutable, as in strings have immutability.  A string can be reassigned, but an INDEX of a string can NOT change.  Reassign all of none of it

# useful methods
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))

# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/python_ref_string.asp
