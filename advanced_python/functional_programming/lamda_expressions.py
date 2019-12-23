# Lambda expressions, used for functions only used once, ANONYMOUS functions
from functools import reduce

# lambda param: action(param)


my_list = [1, 2, 3]


def multiply_by_2(item):
    return item * 2


def check_if_odd(item):
    return item % 2 != 0


def accumulator(acc, item):  # acc defaults to 0 if not given
    print(acc, item)
    return acc + item


print(list(map(lambda item: item * 2, my_list)))  # using lambda instead of multiply_by_2 function
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list, 0))
print(my_list)
