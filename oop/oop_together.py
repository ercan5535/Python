import csv

class Item:
    # Class level attributes
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equalt to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})"

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # Methods
    @classmethod
    def instantiate_from_csv(cls):
        with open('oop/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(name=item['name'],
                 price=float(item['price']),
                 quantity=float(item['quantity'])
            )

    @staticmethod
    def is_num_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Encapsulation
    @property
    def price(self):
        return self.__price

    @property
    # Property Decorator = Read - Only Attribute 
    def name(self):
        print("Getter of name is called")
        return self.__name

    @name.setter
    def name(self, value):
        print("setter of name is called")
        if len(value) > 15:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    # Data Abstraction
    # __ for make these methods not be reachable, 
    # only send_email is reachable
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello, 
        We have {self.__name} {self.quantity} times.
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("smtp")
        body = self.__prepare_body()
        self.__send()
        print(body)
        print("Mail has been sent")
        pass


# Inheritance
class Phone(Item):
    def __init__(self, name:str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have acces to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to received arguments(only for broken_phones, others checked from Item class)
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

item4 = Item("Mouse", 50, 5)
phone1 = Phone("Phonev10", 500, 5, 1)

phone1.apply_increment(0.2)
phone1.send_email()


print(Item.all)
# [Item('Mouse', 50, 5), Phone('jscPhonev10', 500, 5)]

