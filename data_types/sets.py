# Sets data structure
# Unordered collections of UNIQUE objects
# set methods https://www.w3schools.com/python/python_ref_set.asp
# my_set = {1, 2, 3, 4, 5, 5}
# print(my_set)
#
# # Convert list (array) to set to get rid of duplicates
#
# my_list = [1, 2, 3, 3, 4, 5, 6, 8, 8, 8, 8]
# print(set(my_list))
#
# # see if object exists
# print(1 in my_set)
# print(len(my_set))
# print(list(my_set))

my_set = {1,2,3,4,5}
your_set={4,5,6,7,8,9,10}

print(my_set.difference(your_set))
# print(my_set)
# print(my_set.discard(5))
# print(my_set.difference_update(your_set))
# print(my_set)
# print(my_set.intersection(your_set))
# or use alternate way for intersection
# print(my_set & your_set)
# print(my_set.isdisjoint(your_set))
# my_set = {4,5}
# entirety of my_set is in your_set
# print(my_set.issubset(your_set))
# superset is to see if all of my_set is in your_set
# print(your_set.issuperset(my_set))
# my_set = {1,2,3,4,5}
# print(my_set.union(your_set))
# or use alternate way for union
# print(my_set | your_set)
