# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
a = "aaaabbbbbbccccc"
my_counter = Counter(a)
print(my_counter)
# Counter({'b': 6, 'c': 5, 'a': 4})
print(my_counter.keys())
# dict_keys(['a', 'b', 'c'])
print(my_counter.values())
# dict_values([4, 6, 5])
print(my_counter.most_common(1))
# [('b', 6)]
print(my_counter.most_common(2))
# [('b', 6), ('c', 5)]
print(list(my_counter.elements()))
# ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c']


# namedtuple
Point = namedtuple('Pointsss', 'x,y')
pt = Point(1, -4)
print(pt)
# Pointsss(x=1, y=-4)
print(pt.x, pt.y)
# 1 -4

# OrderedDict No key Error!
d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d)
# defaultdict(<class 'list'>, {'a': 1, 'b': 2})

print(d[5])
# []

# deque
d = deque()

d.append(1)
d.append(2)
print(d)
# deque([1, 2])

d.appendleft(3)
print(d)
# deque([3, 1, 2])

d.pop()
print(d)
# deque([3, 1])

d.popleft()
print(d)
# deque([1])

d.extend([4, 5, 6])
print(d)
# deque([1, 4, 5, 6])

d.extendleft([8, 9, 10])
print(d)
# deque([10, 9, 8, 1, 4, 5, 6])

d.rotate(2)
print(d)
# deque([5, 6, 10, 9, 8, 1, 4])

d.rotate(-2)
print(d)
# deque([10, 9, 8, 1, 4, 5, 6])
