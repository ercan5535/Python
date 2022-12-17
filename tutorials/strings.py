# Strings: ordered, immutable, text representation
my_string = "Hello World"
my_string = 'Hello World'
my_string = """Hello World"""

my_string2 = 'I\'m a programmer'
my_string2 = "I'm a programmer"

my_string3 = """Hello
World"""
print(my_string3)
# Hello
# World

my_string3 = """Hello \
World"""
print(my_string3)
# Hello World

my_string3 = "Hello \
World"
print(my_string3)
# Hello World

my_string = "Hello World"
print(my_string[0])
# H

#my_string[0] = "a"
# TypeError: 'str' object does not support item assignment

print(my_string[::2])
# HloWrd
print(my_string[::-1])
# dlroW olleH

print(my_string.lower())
# hello world
print(my_string.upper())
# HELLO WORLD

print(my_string.startswith("H"))
# True
print(my_string.startswith("D"))
# False

print(my_string.find("o"))
# 4

print(my_string.find("lo"))
# 3

print(my_string.find("asd"))
# -1

print(my_string.count("o"))
# 2

print(my_string.replace("World", "Universe"))
# Hello Universe

print(my_string.replace("Worasdsadsald", "Universe"))
# Hello World

my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)
# ['how', 'are', 'you', 'doing']

new_string = " ".join(my_list)
print(new_string)
# how are you doing

#Formatting
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)
# the variable is Tom

print("%d %.2f" % (2, 2.154))

a = 2
b=2.14
print("the variables are {} and {:.2f}".format(a,b))

print(f"the variables are {a} and {b:.2f}")