li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, True]
# Data structure (list, similar to arrays)

amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])

# List Slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
amazon_cart[0] = 'laptop'
# If new_cart = amazong_cart is used then changing new_cart will change amazon_cart since it is same space in memeory
# using list splicing creates new list, so it is a copy and not direct reference to memory (see below)
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
print(new_cart[0:2])
# Lists ARE mutable

# ************************************** MATRIX ***********************************************
#  2D list, lists in a list
matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9]
]
print(matrix[0][0])
print(matrix[0][2])
# ************************************** METHODS ***********************************************
# https://www.w3schools.com/python/python_ref_list.asp

# Adding append
basket = [1, 2, 3, 4, 5]
print(basket)
new_list = basket.append(100)
# ^ new_list is NONE because append changes the list in place, does not create a result
print(basket)
print(new_list)
basket.insert(4, 100)
print(basket)
basket.extend([100, 101])
print(basket)

# Removing
basket.pop()
print(basket)
basket.pop(0)
print(basket)
basket.remove(4)
print(basket)
new_list = basket.pop()
print(new_list)

new_list = basket.clear()
print(basket)

# Index
basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('d', 0, 4))
# Python keywords https://www.w3schools.com/python/python_ref_keywords.asp
basket = ['a', 'b', 'c', 'd', 'e', 'd']
print('d' in basket)
print('x' in basket)
print(basket.count('d'))

# sort
basket.sort()
print(basket)
basket = ['a', 'b', 'x','c', 'd', 'e', 'd']
print(sorted(basket))
# sorted CREATES NEW ARRAY
new_basket = basket.copy() #Will also make a copy like slicing
new_basket.sort()
new_basket.reverse()
print(new_basket)
print(new_basket[::-1])

# create list with range and join
print(list(range(1,100)))
# sentence = '! '
# new_sentence = sentence.join(['hi','this', 'is', 'awesome'])
# print(new_sentence)
# short way
new_sentence = ' '.join(['hi','this', 'is', 'awesome'])
print(new_sentence)

# List unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)