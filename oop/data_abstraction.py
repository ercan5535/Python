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

phone1 = Item("Phonev10", 500, 5)

phone1.send_email()