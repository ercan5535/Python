# Dictionary: Key-Value pairs, Unordered, Mutable
my_dict = {"name": "Max", "age": 28, "city": "Boston"}
# or
my_dict2 = dict(name="Marry", age=27, city="Boston")

print(my_dict, my_dict2, sep="\n")
# {'name': 'Max', 'age': 28, 'city': 'Boston'}
# {'name': 'Marry', 'age': 27, 'city': 'Boston'}

value = my_dict["age"]
# 28

#value = my_dict["last_name"]
# KeyError: 'lastname'

my_dict["email"] = "asd@asd"
print(my_dict)
# {'name': 'Max', 'age': 28, 'city': 'Boston', 'email': 'asd@asd'}1

del my_dict["name"]
# or my_dict.pop("name")
print(my_dict)
# {'age': 28, 'city': 'Boston', 'email': 'asd@asd'}

keys = my_dict.keys()
values = my_dict.values()
for key, value in my_dict.items():
    continue

# copy a dict
new_dict = my_dict.copy()
new_dict = list(my_dict)

# merge 2 dict
my_dict.update(my_dict2)
print(my_dict) #on the same keys, updated with my_dict2's values
# {'age': 27, 'city': 'Boston', 'email': 'asd@asd', 'name': 'Marry'}