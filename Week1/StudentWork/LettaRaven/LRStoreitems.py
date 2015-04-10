# author - LettaRaven

# This is a store to buy items
# Item, order, buyer, qty, price

# I am feeling better with this exercise. I knew what I wanted to do and was on the right track, just starting out of order.
# It made me stop and look a few things up because I knew what I wanted to do but was second guessing myself. Now I can
# articulate a little better why my mind leaps to something in particular.

# I have no idea why this isn't working

class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Line():
    def __init__(self, qty, item):
        self.qty = qty
        self.line_item = item

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

store = Store("House of Bunnies")

item = Item("Bunny W Ray Gun", 5.99)
store.products.append(item)

buyer = Buyer("Anna")
store.customers.append(buyer)

line = Line(1, store.products[0])
buyer.cart.lines.append(line)

print(buyer.cart.total())


