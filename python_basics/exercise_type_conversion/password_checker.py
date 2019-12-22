username = input('Enter your username')
password = input('Enter your password')

pass_len = len(password)
coded_pass = '*' * pass_len

print(f'{username}, your password {coded_pass} is {pass_len} letters long')
