# Tuple Data Structure
# immutable list
# methods https://www.w3schools.com/python/python_ref_tuple.asp

my_tuple = (1, 2, 3, 4, 5,1)
print(5 in my_tuple)
user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user[(1, 2)])

# assign variables to part of tuple
x, y, z, *other = (1, 2, 3, 4, 5)
print(other)

# count
print(my_tuple.count(1))
# index
print(my_tuple.index(1))
# len
print(len(my_tuple))
