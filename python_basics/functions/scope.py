#What variables do I have access to?
# A new function is kind of like creating a new world for scope

# 1 - Start with local
# 2 - Parent local scope
# 3 - Global
# 4 - built in python functions

# global keyword uses the global variable
# dependency injection is better (parameters needed)

# nonlocal keyword

# Scope - what variables do I have access to?
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
# nonlocal is useful for closures
#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions