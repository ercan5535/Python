# shallow copy: one level deep, only references of nested child objects
# deep copy: full independent copy

org = 5
copy = org
copy = 6
print(copy)
# 6
print(org)
# 5


org = [0, 1, 2, 3, 4]
copy = org
copy[0] = -10
print(copy)
# [-10, 1, 2, 3, 4]
print(org)
# [-10, 1, 2, 3, 4]


import copy

org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
# or copy = org.copy()
# or copy = list(org)
# or copy = org[:]
cpy[0] = -10
print(cpy)
# [-10, 1, 2, 3, 4]
print(org)
# [0, 1, 2, 3, 4]


org = [[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(cpy)
# [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]
print(org)
# [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]
# becaues of shallow copy, only one level deep
# so we need deep copy
org = [[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
# [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]
print(org)
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person('Alex', 27)
p2 = p1
p2.age = 28
print(p1.age)
# 28
print(p2.age)
# 28

p1 = Person('Alex', 27)
p2 = copy.copy(p1)
p2.age = 28
print(p1.age)
# 27
print(p2.age)
# 28
# shallow copy works!

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 58)
p2 = Person('Joe', 27)

company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 55
print(company.boss.age)
# 55
print(company_clone.boss.age)
# 55
# Shallow copy doesnt work
# So we need deep copy


p3 = Person('Alex', 58)
p4 = Person('Joe', 27)
company2 = Company(p3, p4)
company_clone2 = copy.deepcopy(company2)
company_clone2.boss.age = 55
print(company2.boss.age)
# 58
print(company_clone2.boss.age)
# 55
# Deep copy works!