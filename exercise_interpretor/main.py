import translators

try:
    with open('translatethis.txt', mode='r') as my_file:
        print(my_file.read())
        my_file.seek(0)
        print(translators.google(my_file.read(), from_language='en', to_language='ja'))
except FileNotFoundError as err:
    print('File does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err


# text = input('What do you want to translate to japanese?')
# print(translators.google(text, from_language='en', to_language='ja'))
