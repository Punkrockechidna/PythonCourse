# This is better to use than just open, this also doesn't require close :)
with open('test.txt', mode ='w') as my_file:
    text = my_file.write('It\'s a mario')
    # print(my_file.readlines())
    print(text)

# mode 'r' is default (read)
# mode 'r+' is reading and writing

# append mode is with an "a" and it adds to the end of the file
# mode w is to write and overwrites file

# Create a file that doesn't exist with write as well "w"
with open('sad.txt', mode ='w') as my_file:
    text = my_file.write(':(')
    # print(my_file.readlines())
    print(text)