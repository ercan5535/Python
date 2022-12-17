# lambda arguments: expresssion

add10 = lambda x: x+10
print(add10(5))
# 15

mult = lambda x,y: x*y
print(mult(2,5))
# 10

point2D = [(1,2), (15,1), (5,-1), (10,4)]

print(sorted(point2D))
# [(1, 2), (5, -1), (10, 4), (15, 1)]

print(sorted(point2D, key=lambda x:x[1]))
# [(5, -1), (15, 1), (1, 2), (10, 4)]

print(sorted(point2D, key=lambda x:x[0]+x[1]))
# [(1, 2), (5, -1), (10, 4), (15, 1)]

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))
# [2, 4, 6, 8, 10]

c = [x*2 for x in a]
print(c)
# [2, 4, 6, 8, 10]

b = filter(lambda x: x%2==0, a)
print(list(b))
# [2, 4]

c = [x for x in a if x%2==0]
print(c)
# [2, 4]

from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)
# 24