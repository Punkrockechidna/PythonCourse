is_old = True
is_licensed = True

if is_old and is_licensed:
    print('you are old enough to drive and you have a license')
#     elif can be used as else if
else:
    print('you are not of age')

print('okokok')

# Truthy falsey https://docs.python.org/2.4/lib/truth.html

# ternary operator or conditional expression
# condition_if_true if condition else condition_if_else
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

# Short circuiting uses OR, if statement stops reading condition if the first parameter is true/false
# depending on or/and
