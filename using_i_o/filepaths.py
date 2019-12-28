with open('./app/sad.txt', mode='r') as my_file: # <----relative path  ./ means from current folder  ../ means back a folder
    print(my_file.read())


# C:\Users\Dan\code\python\PythonCourse\using_i_o\app       <----- Absolute path