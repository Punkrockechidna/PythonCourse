# parameters
# default parameters

def say_hello(name='Darth Vader', emoji="*"):
    print(f'Helloooo {name} {emoji}')


say_hello()
# positional arguments
say_hello('Andrei', '888')

# keyword arguments
say_hello(name='AV', emoji='XD')


# *args **kwargs

def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func('Andy', 1, 2, 3, 4, 5, num1=5, num2=10))

# Rule order: params, *args, default parameters, **kwargs
