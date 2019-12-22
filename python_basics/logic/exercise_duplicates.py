# print duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
unique_list = set(some_list)


for item in some_list:
    if item in unique_list:
        unique_list.remove(item)
    else:
        print(item)

# Without sets
some_list.sort()
print(some_list)

for number in range(len(some_list)):
    if some_list[number] == some_list[number-1]:
        print(some_list[number])

# Andrei way
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)