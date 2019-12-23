# ZIP

# previous version
# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(items * 2)
#     return new_list

# using zip
my_list = [1, 2, 3]
your_list = [10,20,30]
their_list = (5,4,3)


def multiply_by_2(item):
    return item * 2


def check_if_odd(item):
    return item % 2 != 0



print(list(zip(my_list, your_list,their_list))) #not calling function, just running it

# combines into tuple based on location in list/tuple