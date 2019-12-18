# Datatype dict (Dictionary), also known as hash table, map, object
# Data Structure as well
# unordered key-value pair
# dict methods https://www.w3schools.com/python/python_ref_dictionary.asp

dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}
my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'x': True
    }
]
print(dictionary['a'][1])
print(my_list[0]['a'][2])

# Alternate way of making dictionary
user = dict(name='JohnJohn')
print(user)

# See if key exists
user2 = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}
print(user2.get('age', 21))
# another way
print('basket' in user2.keys())
# See if valuye exists
print('hello' in user2.values())
# see all items in dict
print(user2.items())
# empty the dictionary
user2.clear()
# copy a dict
user3 = user.copy()
print(user3)

# popitem is useful to destructively iterate over a dict

# update adds missing key or modifies existing one
print(user.update({'ages': 55}))
print(user)
