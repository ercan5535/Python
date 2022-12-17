# Errors and Exceptions

try: eval('a=5 print(a)')
except SyntaxError: pass

try: a = 5 + "10"
except TypeError: pass

try: import moduleasd
except ModuleNotFoundError: pass

try: b=c
except NameError: pass

try: open('somefile.txt')
except FileNotFoundError: pass

try: a=[1,2,3]; a.remove(5)
except ValueError: pass

try: a[4]
except IndexError: pass

try: my_dict={'name': 'max'}; my_dict['age']
except KeyError: pass

try: a=5/0
except Exception as e: print(e)
# division by zero

try: a=5/1; b=a+"10"
except ZeroDivisionError as e: print(e)
except TypeError as e: print(e)
# division by zero

try: a=5/0; b=a+"10"
except ZeroDivisionError as e: print(e)
except TypeError as e: print(e)
# unsupported operand type(s) for +: 'float' and 'str'

try: a=5/1; b=a+10
except ZeroDivisionError as e: print(e)
except TypeError as e: print(e)
else: print("Everything is fine")
# Everything is fine

try: a=5/1; b=a+10
except ZeroDivisionError as e: print(e)
except TypeError as e: print(e)
else: print("Everything is fine")
finally: print("Cleaning up")
# Everything is fine
# Cleaning up

x = 5
if x < 0:
    raise ValueError("x should be positive")

assert (x>0), "x should be positive"

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x>1000:
        raise(ValueTooHighError("Value is too high"))
    if x<10:
        raise(ValueTooSmallError("Value is too small", x))

try: test_value(2000)
except ValueTooHighError as e: print(e)
# Value is too high

try: test_value(5)
except ValueTooSmallError as e: print(e)
# ('Value is too small', 5)