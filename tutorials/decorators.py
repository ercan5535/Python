def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')

print_name()
# Alex

print_name = start_end_decorator(print_name)
print_name()
# Start
# Alex 
# End 

@start_end_decorator
def print_name2():
    print('Alex')

print_name2()
# Start
# Alex
# End


def start_end_decorator2(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result=func(*args, **kwargs)
        print('End')
        return result
    return wrapper
    
@start_end_decorator2
def add5(x):
    return x+5

print(add5(5))
# Start
# End
# 10

print(help(add5))
print(add5.__name__)
#Help on function wrapper in module __main__:

#wrapper(*args, **kwargs)

#None
#wrapper

import functools
from unittest import result

def start_end_decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result=func(*args, **kwargs)
        print('End')
        return result
    return wrapper
    
@start_end_decorator3
def add5(x):
    return x+5

print(help(add5))
print(add5.__name__)
#Help on function add5 in module __main__:

#add5(x)

#None
#add5

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')

greet('Alex')
# Hello Alex
# Hello Alex
# Hello Alex
# Hello Alex


def start_end_decorator4(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator4
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

say_hello('MAX')
# Calling say_hello('MAX')
# Start
# Hello MAX
# End
# 'say_hello' returned 'Hello MAX'


class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello')

say_hello()
# This is executed 1 times
say_hello()
# This is executed 2 times
say_hello()
# This is executed 3 times