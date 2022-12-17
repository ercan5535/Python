# itertools: product, permutations, combinations, accumulate, groupby, infinite iterators

from itertools import product, permutations, combinations,\
    combinations_with_replacement, accumulate, groupby,\
    count, cycle, repeat
import operator

a=[1, 2, 3]
b=[3]
print(list(product(a,b)))
# [(1, 3), (2, 3), (3, 3)] kartesian product

print(list(product(a,b, repeat=2)))
# [(1, 3, 1, 3), (1, 3, 2, 3), (1, 3, 3, 3), (2, 3, 1, 3), (2, 3, 2, 3), (2, 3, 3, 3), (3, 3, 1, 3), (3, 3, 2, 3), (3, 3, 3, 3)] kartesian product

print(list(permutations(a)))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

print(list(combinations(a, 2)))
# [(1, 2), (1, 3), (2, 3)]

print(list(combinations_with_replacement(a,2)))
# [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

print(list(accumulate(a, func=operator.mul)))
# [1, 3, 6] accumulate sum

print(list(accumulate(a, func=operator.mul)))
# [1, 2, 6] accumulate sum

group_obj = groupby(a, key=lambda x: x<2)
for key, value in group_obj:
    print(key, list(value))
# True [1]
# False [2, 3]

persons = [{"name": "Tim", "age": 25}, {"name": "Dan", "age": 25},
            {"name": "Lisa", "age": 27}, {"name": "Claire", "age": 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))
# 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# 27 [{'name': 'Lisa', 'age': 27}]
# 28 [{'name': 'Claire', 'age': 28}]

# Infinite iterating
for i in count(10):
    print(i)
    break
# 10 11 12...

for i in cycle([1,2,3]):
    print(i)
    break
# 1 2 3 1 2 3 1 2 3 1 2

for i in repeat(1):
    print(i)
    break
# 1 1 1 1 1 1 1 1 1 1 1