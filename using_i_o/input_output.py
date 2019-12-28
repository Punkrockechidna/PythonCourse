my_file = open('app/test.txt')
print(my_file.read())
# Can only read file once, cursor is at end of file after opening
my_file.seek(0)
# this resets cursor to start of file
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())

# Must always close the file
my_file.close()