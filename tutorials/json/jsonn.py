import json
person={"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON, type(personJSON))
# <class 'str'>

with open('json/person.json', 'w') as file:
    json.dump(person, file, indent=4)
# saved into file

print(json.loads(personJSON), type(json.loads(personJSON)))
# <class 'dict'>

with open("json/example.json", "r") as file:
    ex_json = json.load(file)
    print(ex_json)


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

# userJSON = json.dumps(user)
# Object of type User is not JSON serializable
# we should encode, first way:
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")
userJSON=json.dumps(user, default=encode_user)
print(userJSON)
# {"name": "Max", "age": 27, "User": true}

# second way:
from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)
# {"name": "Max", "age": 27, "User": true}

userJSON = UserEncoder().encode(user)
print(userJSON)
# {"name": "Max", "age": 27, "User": true}

user = json.loads(userJSON)
print(user)
# {'name': 'Max', 'age': 27, 'User': True} dict

