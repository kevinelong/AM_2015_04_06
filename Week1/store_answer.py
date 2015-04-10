class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Line():
    def __init__(self, qty, item):
        self.qty = qty
        self.item = item

    def extension(self):
        return self.qty * self.item.price


class Order():
    def __init__(self):
        self.lines = []

    def total(self):
        subtotal = 0
        for line in self.lines:
            subtotal = subtotal + line.extension()
        return subtotal


class Store():
    def __init__(self, name):
        self.name = name
        self.products = []
        self.customers = []


class Buyer():
    def __init__(self, id):
        self.id = id
        self.cart = Order()


store = Store("amazon")

item = Item("PC Game Programming Explorer", 39.99)
store.products.append(item)

buyer = Buyer("kevin")
store.customers.append(buyer)

line = Line(2, store.products[0])
buyer.cart.lines.append(line)

print(buyer.cart.total())
