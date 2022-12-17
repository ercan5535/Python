def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()


value = next(g)
print(value)
# 1
value = next(g)
print(value)
# 2
value = next(g)
print(value)
# 3
# value = next(g)
# print(value)
# StopIteration Error
# print(list(g))
# StopIteration Error

print(sum(g))
# 6


def countdown(num):
    print('Starting')
    while num>0:
        yield num
        num-=1

cd = countdown(4)
# didnt print anything

print(next(cd))
# Starting
# 4
print(next(cd))
# 3
print(next(cd))
# 2
print(next(cd))
# 1
# print(next(cd))
# StopIteration

from re import A
import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num +=1

print(list(firstn(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(firstn_generator(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# generator no need a list and way ligther
print(sys.getsizeof(firstn(1000000)))
# 448728
print(sys.getsizeof(firstn_generator(1000000)))
# 200

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print(list(fibonacci(20)))
# [0, 1, 1, 2, 3, 5, 8, 13]

mygenerator = (i for i in range(1000000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))
# 208

mylist = [i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(mylist))
# 4167352