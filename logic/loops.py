# Iterables - list, dictionary, yuple, set, string.  One by one check each item in collection
user = {
    'name': "golem",
    "age": 5006,
    'can_swim': False
}

for item in user.items():
    print(item)
# or use this way
for key, value in user.items():
    # can use k and v
    print(key, value)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)
