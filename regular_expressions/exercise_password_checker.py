# at least 8 characters
# contain any sort of letters, numbers, $@#%
# ends with a  number

import re

passw = input("Enter a password with 8+ char ending with num")
password = re.compile(r"^[\w\d\@*\#*\$*\%*]{8,}\d$")

checker = password.search(passw)
good_pass = False
while not good_pass:
    if checker:
        break
    else:
        passw = input("Enter a password with 8+ char ending with num")
        checker = password.fullmatch(passw)
        continue
