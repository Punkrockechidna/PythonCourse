# MAP

# previous version
# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(items * 2)
#     return new_list

# using map
def multiply_by_2(item):
    return item * 2


print(list(map(multiply_by_2, [1, 2, 3]))) #not calling function, just running it
