# REDUCE

# previous version
# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(items * 2)
#     return new_list

# using reduce
from functools import reduce

my_list = [1, 2, 3]


def multiply_by_2(item):
    return item * 2


def check_if_odd(item):
    return item % 2 != 0


def accumulator(acc, item):  # acc defaults to 0 if not given
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))  # not calling function, just running it

# reduces list to one value
