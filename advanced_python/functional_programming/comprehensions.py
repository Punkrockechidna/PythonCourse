# list, set, dictionary
# quick way to create instead of looping

# comprehension way
my_list = [char for char in "hello"]
my_list2 = [num for num in range(0, 100)]
my_list3 = [num ** 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]  # harder to read

# loop method
# for char in 'hello':
#     my_list.append(char)

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# ******************************************* Set and Dict *******************************************
# Set uses {} instead of []
simple_dict = {
    'a': 1,
    'b': 2
}
# ******** What we want to do to data ******** extract key and value
my_dict = {key: value ** 2 for key, value in simple_dict.items()}
my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict)
print(my_dict2)