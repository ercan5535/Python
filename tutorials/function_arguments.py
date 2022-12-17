def foo(a, b, c, d=4):
    print(a, b, c, d)

foo(1, b=2, c=3)
# 1 2 3 4

# foo(1, b=2, 3)
# SyntaxError: positional argument follows keyword argument

# foo(1, b=2, a=1)
# TypeError: foo() got multiple values for argument 'a'

def foo2(a, b, *args, **kwargs):
    # args is tuple
    # kwargs is dictionary
    print(a, b)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

foo2(1, 2)
# 1 2

foo2(1, 2, 3, 4, 5, six=6, seven=7)
# 1 2
# 3
# 4
# 5
# six 6
# seven 7

def foo3(a, b, *, c, d):
    print(a, b, c, d)

# foo3(1, 2, 3, 4)
# TypeError: foo3() takes 2 positional arguments but 4 were given

foo3(1, 2, c=3, d=4)
# 1 2 3 4

def foo4(*args, last):
    for arg in args:
        print(arg)
    print(last)

# foo4(1, 2, 3)
# foo4() missing 1 required keyword-only argument: 'last'

foo4(1, 2, 3, last=4)
# 1
# 2 
# 3
# 4

def foo5(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
my_tuple = (0, 1, 2)
my_dict = {'a': 1, 'b': 2, 'c':3}
foo5(*my_list)
# 0 1 2
foo5(*my_tuple)
# 0 1 2
foo5(**my_dict) # keys should match
# 1 2 3

def foo6():
    global number
    x = number
    number = 3
    print('number inside function:', x)

number = 0
foo6()
# number inside function: 0
print(number)
# 3

def foo7(x):
    x = 5

var = 10
foo7(var)
print(var)
# 10
# Immutable dtypes can not be changed
# int, float, decimal, bool, string, tuple, and range.

def foo8(a_list):
    a_list.append(4)

my_list = [1, 2, 3]
foo8(my_list)
print(my_list)
# [1, 2, 3, 4]
# Mutable dtypes can be changed
# list, dictionary, set and user-defined classes.

def foo9(a_list):
    a_list = [100, 200, 300]
    a_list.append(4)

my_list = [1, 2, 3]
foo9(my_list)
print(my_list)
# [1, 2, 3]
# didnt change

def foo10(a_list):
    a_list += [100, 200, 300]

my_list = [1, 2, 3]
foo10(my_list)
print(my_list)
# [1, 2, 3, 100, 200, 300]

def foo11(a_list):
    a_list = a_list + [100, 200, 300]

my_list = [1, 2, 3]
foo11(my_list)
print(my_list)
# [1, 2, 3]
# didnt change
