for i, char in enumerate('Helllooo'):
    print(i, char)
# prints
# 0 H
# 1 e
# 2 l
# 3 l
# 4 l
# 5 o
# 6 o
# 7 o

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')
