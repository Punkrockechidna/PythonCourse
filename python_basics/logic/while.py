i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('Done with all the work!')

# for loop vs while

# simpler
my_list = [1, 2, 3]
for item in my_list:
    print(item)

# more flexible and powerful
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# breaking
while True:
    response = input('say something: ')
    if response == 'hi':
        break

# continue. continue goes back to the beginning of the loop (for or while)
my_list = [1, 2, 3]
for item in my_list:
    continue
    print(item)

# Pass, not very useful. passes to next line, but good for placeholder in the loop
for item in my_list:
    # need code in indent, pass will fill req
    pass
