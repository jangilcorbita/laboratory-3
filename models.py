from abc import ABC

class Person(ABC):
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone
    
    @property
    def name(self):
        return self._name

class Customer(Person):
    def __init__(self, customer_id, name, phone, address):
        super().__init__(name, phone)
        self.customer_id = customer_id
        self.address = address

class MenuItem(ABC):
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class Food(MenuItem):
    pass

class Beverage(MenuItem):
    pass

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.status = "Pending"
        self.total = 0.0

    def add_item(self, item):
        self.items.append(item)
        self.total += item.price