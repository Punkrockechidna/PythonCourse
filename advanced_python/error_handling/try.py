# Error Handling

while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a number greater than 0')
    else:
        print('Thank you!')
        break
    finally:
        print('ok, I am finally done') #runs regardless at end of everything


# *********************************************************************************************************************
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err: #can use multiple errors in ()
        print(f'Please enter numbers {err}') #needs to pass this way


print(sum(1, 2))

# *********************************************************************************************************************
# Throw our own err by using:
raise ValueError('Hey, cut it out')