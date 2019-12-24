# iterable
# iterate
# generator
# generators are iterable, not all iterables are generators

# generators go 1 at a time, saves memory.  range is a generator


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

def generator_function(num):
    for i in range(num):
        yield i*2 #pauses function and comes back to it when next keyword used
#         ^ made our own generator

g = generator_function(100)
next(g)
next(g)
print(next(g))

# for item in generator_function(1000):
#     print(item)

# instead of creating a whole list in memory like the commented code above, generator creates item 1 by 1

# Example long_time is faster than long_time2

from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i*5


long_time()
long_time2()