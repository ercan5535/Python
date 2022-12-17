# -We use getters & setters to add validation logic around 
# getting and setting a value.
# -To avoid direct access of a class field i.e. private variables 
# cannot be accessed directly or modified by external user.


class Item:

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equalt to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity


item1 = Item("MyItem", 750)

item1.name = "OtherItem"

print(item1.name)
# OtherItem


# To make this attribute read-only argument. 
# Add property decorator to class for this attribute

class Item2:

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equalt to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    # Property Decorator = Read - Only Attribute 
    def name(self):
        return self.__name


item2 = Item2("MyItem", 750)
 
# item2.name = "OtherItem"
# AttributeError: property 'name' of 'Item2' object has no setter

item2.__name = "OtherItem"
# But it works!
print(item2.__name)
# OtherItem
# more detail:
# https://stackoverflow.com/questions/14594120/when-should-an-attribute-be-private-and-made-a-read-only-property

"""
Per PEP 8:

Use one leading underscore only for non-public
 methods and instance variables.

No underscore: it's a public variable.
One underscore: it's a protected variable.
Two underscores: it's a private variable.
"""



class Item3:

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equalt to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    # Property Decorator = Read - Only Attribute 
    def name(self):
        print("Getter of name is called")
        return self.__name

    @name.setter
    def name(self, value):
        print("setter of name is called")
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

item3 = Item3("MyItem", 750)

item3.name = "OtherItem"
# setter of name is called

# item3.name = "OtherItemmmmm"
# Exception: The name is too long!