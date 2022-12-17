# Tuple: ordered, immutable, allows duplicate elements
# Because of being immutable, tuples are easier than lists to handle
my_tuple = ("Max", 28, "Boston") 
# or my_tuple = "Max", 28, "Boston"
# or my_tuple = tuple(["Max", 28, "Boston"])

print(type(("Max")))
# class 'str'

print(type(("Max",)))
# class 'tuple'

print(my_tuple[0])
#  Max

# my_tuple[0] = "Tim"
# TypeError: 'tuple' object does not support item assignment

print(my_tuple.count("Max"))
#  1

print(my_tuple.index("Max"))
#  0

my_list = list(my_tuple)
my_tuple = tuple(my_list)

name, age, city = my_tuple
print(name, age, city)
# Max 28 Boston

my_tuple = (1, 2, 3 , 4, 5, 6)
v1, *v2, v3 = my_tuple
print(v1, v2, v3)
# 1 [2, 3, 4, 5] 6
