import random

# random float 0 - 1
print(random.random())
# 0.1719906757330274

print(random.uniform(1, 10))
# 5.160712183410864

# upper bound included
print(random.randint(1, 10))
# 8

# upper bound not included
print(random.randrange(1, 10))
# 2

# normal distribution
print(random.normalvariate(0, 1))
# 1.1266858584040171

print(random.choice(list("ABCDEFGH")))
# H

print(random.choices(list("ABCDEFGH"), k=3))
# ['G', 'G', 'H']

# sample only unique
print(random.sample(list("ABCDEFGH"), 3))
# ['F', 'E', 'A']

my_list = list("ABCDEFGH")
random.shuffle(my_list)
print(my_list)
# ['A', 'D', 'E', 'F', 'C', 'B', 'G', 'H']


random.seed(1)
print(random.random())
print(random.randint(1, 10))
#0.13436424411240122
#2

random.seed(1)
print(random.random())
print(random.randint(1, 10))
#0.13436424411240122
#2

import secrets

print(secrets.randbelow(10))
# 4

# max 1111=15
print(secrets.randbits(k=4))
# 1 

print(secrets.choice(list("ABCDEFGH")))
# F

import numpy as np

print(np.random.rand(3))
# [0.54810443 0.90132572 0.30055787]

print(np.random.rand(3,3))
# [[0.27385054 0.27583215 0.96628366]
#  [0.52769974 0.1007573  0.77281637]
#  [0.82061461 0.71059648 0.46433087]]

print(np.random.randint(0, 10, 4))
# [5 1 9 6]

print(np.random.randint(0, 10, (2,2)))
# [[9 3]
#  [1 3]]

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
np.random.shuffle(arr)
print(arr)

np.random.seed(1)