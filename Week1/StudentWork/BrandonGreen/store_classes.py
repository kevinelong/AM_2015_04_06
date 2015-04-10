

class Order():
    def __init__(self, buyer, date):
        self.buyer = buyer
        self.date = date
        self.order_list = []

    def add_to_order(self, line_item):
        self.order_list.append(line_item)

    def get_total(self):
        total = 0
        for order in self.order_list:
            total += order.item.price * order.qty
        return total


class LineItem():
    def __init__(self, qty, item):
        self.qty = qty
        self.item = item


class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class Buyer():
    def __init__(self, user_name, payment, shipping):
        self.user_name = user_name
        self.payment = payment
        self.shipping = shipping

    def __str__(self):
        return self.user_name


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

e_book = Item('A Game of Classes', 7.99)

branook.add_customer(brandon)

branook.customer_list()

my_purchase = LineItem(2, e_book)

my_order = Order(brandon, 'today')

my_order.add_to_order(my_purchase)

print my_order.get_total()





