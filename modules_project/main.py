# import utility
# import shopping.shopping_cart
# or
# from shopping.shopping_cart import buy
from utility import multiply,divide #always try to be explicit like this
# or
from shopping import shopping_cart #a nice,preffered way

# print(utility)
print(shopping_cart.buy('apple'))
print(divide(5,2))
print(multiply(5,2))