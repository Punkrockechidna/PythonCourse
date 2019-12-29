import re

string = 'search this inside of this text please!'

print('search' in string) #non regular expression

# print(re.search('this',string))
a = re.search('this',string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())

# b = re.search('thIs',string)
# print(b.span()) #doesn't exist, throws AttributeError

pattern = re.compile(r'this') #the r says raw string, ignores symbols python looks for in string
pattern2 = re.compile('search this inside of this text please!')

string2 = 'search this inside of this text please! And extra words'
c = pattern.search(string)
d = pattern.findall(string)
e = pattern2.fullmatch(string) #has to be exact string to match
f = pattern2.match(string2) #sees if there is match and doesn't care if there is extra
print(c)
print(d)
print(e)
print(f)

# ****************************************  Advanced patterns  **************************************
# email validation
r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"