# Fundamental Data Types
# int
print(type(2+4))
print(2-4)
print(2*4)
print(2/4)
# float
# Floating point is base2 scientific notation.  1/3 +1/3 + 1/3 != 1
# https://docs.python.org/3/tutorial/floatingpoint.html

print(2 ** 2)  # ** is to the power of
print(5 // 4)  # // is how many times it goes in a division rounded down
print(6 % 4)  # % this is still modulus, what is the remainder
print(round(3.1))
print(abs(-10))
# Math functions https://www.programiz.com/python-programming/modules/math

# Operator precedence Should be pemdas () ** * / + -

complex  # type of number datatype used for complex math
print(bin(5))  # returns the binary representation
print(int('0b101', 2))  # converts to base 2 then base 10

# ******************************************************************************************************************
# Python best practices for variables
# snake_case
# start with lowercase or underscore
# letters, numbers, underscores
# case sensitive
# don't overwrite keywords
# keywords https://www.w3schools.com/python/python_ref_keywords.asp

# constants are all in capitals
# two underscores are dundle __hihi

a, b, c = 1, 2, 3  # creates 3 variables in quick succession

iq = 100
user_age = iq / 5  # after the = is an EXPRESSION and the whole line is a STATEMENT

# augmented assignment operator += or -= (number)

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
bool
list
tuple
set
dict

# Classes -> custom types


# Specialized Data Types

None
