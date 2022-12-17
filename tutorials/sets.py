# Sets: unordered, mutable, no duplicate

myset = {"Hello"}
# or myset = set([1, 2, 3])
# or myset = {1, 2, 3}
print(myset,type(myset))
# {'Hello'} <class 'set'>

frozen = frozenset([1, 2, 3])
# can not be changed

my_set = set("Hello")
print(my_set)
# {'H', 'e', 'o', 'l'}

new_set = set()

new_set.add(1)
new_set.add(1)
new_set.add(2)
new_set.add("Hello")
print(new_set)
# {'Hello', 1, 2}

new_set.remove(1)
# new_set.remove(4)
# KeyError: 4
# or
new_set.discard(4) # no KeyError: 4
value = new_set.pop()
print(value)
# 2

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
# with inplace odds.update(evens)
print(u)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

i = odds.intersection(evens)
# with inplace odds.intersection_update(evens)
print(i)
# set() empty set

i2 = odds.intersection(primes)
print(i2)
# {3, 5, 7}

diff = odds.difference(primes)
# with inplace odds.differences_update(prime)
print(diff)
# {1, 9}

sym_diff = odds.symmetric_difference(primes)
# with inplace odds.symmetric_difference_update(primes)
print(sym_diff)
# {1, 2, 9}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setC = {1, 2, 3}
setD = {10, 11, 12}

print(setB.issubset(setA))
# False
print(setC.issubset(setA))
# True

print(setA.issuperset(setC))
# True
print(setC.issuperset(setA))
# False

print(setA.isdisjoint(setC))
# False
print(setA.isdisjoint(setD))
# True

set1 = {1, 2, 3}
set2 = set1.copy()
# or
set2 = set(set1)
