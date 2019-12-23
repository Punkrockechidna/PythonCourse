# FILTER

# previous version
# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(items * 2)
#     return new_list

# using filter
my_list = [1, 2, 3]


def multiply_by_2(item):
    return item * 2


def check_if_odd(item):
    return item % 2 != 0


print(list(filter(check_if_odd, my_list))) #not calling function, just running it
