print(4*5)
# 20

print(2**5)
# 32

print([0] * 5)
# [0, 0, 0, 0, 0]

print((0, 1) * 5)
# (0, 1, 0, 1, 0, 1, 0, 1, 0, 1)

print("AB" * 5)
"ABABABABAB"

numbers = (1, 2, 3, 4, 5)
*beginning, last = numbers
# always unpack as list
print(beginning, last)
# [1, 2, 3, 4] 5

my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
print([*my_tuple, *my_set])
# [1, 2, 3, 4, 5, 6]

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
print({*dict_a, *dict_b})
# {'a', 'b', 'd', 'c'}
print({**dict_a, **dict_b})
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}