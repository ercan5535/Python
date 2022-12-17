class Item:
    # Class level attributes
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equalt to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object, Instance level attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
# [Item('Phone', 100, 1), Item('Laptop', 1000, 3), Item('Cable', 10, 5), Item('Mouse', 50, 5), Item('Keyboard', 75, 5)]
# without __repr__
# [<__main__.Item object at 0x000002B993B8F150>, <__main__.Item object at 0x000002B993B8F190>, <__main__.Item object at 0x000002B993B8F1D0>, <__main__.Item object at 0x000002B993B8F210>, <__main__.Item object at 0x000002B993B8F250>]

print(Item.__dict__) # All the attributes for Class level
# {'__module__': '__main__', 'pay_rate': 0.8, 'all': [Item('Phone', 100, 1), Item('Laptop', 1000, 3), Item('Cable', 10, 5), Item('Mouse', 50, 5), Item('Keyboard', 75, 5)], '__init__': <function Item.__init__ at 0x000001B94C228FE0>, 'calculate_total_price': <function Item.calculate_total_price at 0x000001B94C229EE0>, 'apply_discount': <function Item.apply_discount at 0x000001B94C229F80>, '__repr__': <function Item.__repr__ at 0x000001B94C22A020>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}

print(item1.__dict__) # All the attributes for instance level
# {'name': 'Phone', 'price': 100, 'quantity': 1}  