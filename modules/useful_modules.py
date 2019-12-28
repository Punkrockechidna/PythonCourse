from collections import Counter, defaultdict, OrderedDict
import datetime
from time import time
from array import array

li = [1,2,3,4,5,6,7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))
# counts number of times value appears by converting to dict (hash map)
print(Counter(sentence))

# really cool, if looking for key in dict will not error if not exist, allows default value return
dictionary = defaultdict(lambda:'does not exist',{'a':1,'b':2})
print(dictionary['c'])

# retains the order in which things are inserted into dict
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 2
d2['b'] = 1

# datetime/time
print(d2 == d)
print(time())
print(datetime.time(5,45,2))
print(datetime.date.today())
print(time())

# array, more performant than lists
arr = array('i', [1,2,3])

