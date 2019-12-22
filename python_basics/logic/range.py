# very useful for looping

print(range(100))
# range(0, 100)
print(range(0,100))
# range(0, 100)

for number in range(0,100):
    print(number)
# prints out 0 to 99

# if don't care what variable is can us _ as variable, example
for _ in range(0,10):
    print(_)

# comes with 3rd param, which skips

for _ in range(0,10,2):
    print(_)
# prints 0 2 4 6 8

for _ in range(10,0,-1):
    print(_)
# prints 10 9 8 7 6 5 4 3 2 1 0

for _ in range(10,0,-2):
    print(_)
# prints 10 8 6 4 2

for _ in range(2):
    print(list(range(10)))
# prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
