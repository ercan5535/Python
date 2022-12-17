# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]

print(mylist.count("banana"))
# 1


mylist.insert(1, "orange")
# ['banana', 'orange', 'cherry', 'apple']
item = mylist.pop()
print(item)
# "apple"

mylist.remove("cherry")
print(mylist)   
# ['banan', 'apple']

mylist.clear()
print(mylist)  
# []

mylist.reverse()
print(mylist)  
# ['apple', 'cherry', 'banana']

mylist.sort() # inplace
print(mylist)
# ['apple', 'banana', 'cherry']

new_list = sorted(mylist) # not inplace
print(new_list)  
# ['apple', 'banana', 'cherry']

mylist = [0] * 5
print(mylist)  #  [0, 0, 0, 0, 0]

mylist2 = [1, 2, 3]
new_list = mylist + mylist2
print(new_list)
# [0, 0, 0, 1, 2, 3]

# copy a list
new_list = mylist2.copy()
new_list = list(mylist2)
new_list = mylist2[:]

# list comprehension
#[f(x) if condition else g(x) for x in sequence]
#[f(x) for x in sequence if condition]
