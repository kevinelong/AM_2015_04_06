

class Order():
    def __init__(self, buyer, cart, date):
        self.buyer = buyer
        self.cart = cart
        self.date = date
        self.order_list = []


class Cart():
    def __init__(self, line_item):
        self.line_item = line_item
        self.cart_list = []


class LineItem():
    def __init__(self, qty, item):
        self.qty = qty
        self.item = item

    def add_to_order(self, qty, item):
        order = []
        for obj in item:
            for x in range(0, qty):
                order.append(obj)


class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add_to_cart(self, item):
        self.cart = []
        self.item = item
        for x in item:
            self.cart.append(item)


class Quantity():
    def __init__(self, quantity):
        self.quantity = quantity


class Buyer():
    def __init__(self, user_name, payment, shipping):
        self.user_name = user_name
        self.payment = payment
        self.shipping = shipping
        self.cart = []


class Store():
    def __init__(self, name):
        self.name = name
        self.products = []
        self.customers = []

    def customer_list(self):
        for customer in self.customers:
            print customer

    def add_customer(self, customer):
        self.customers.append(customer)


branook = Store('BraNook')

brandon = Buyer('spacefish', 'cash', 'UPS')

