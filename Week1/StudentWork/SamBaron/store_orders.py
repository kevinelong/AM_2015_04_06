__author__ = 'Sam Baron'


class Store(object):

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = {}


    def add_inventory_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name] += quantity
        else:
            self.inventory[item.name] = quantity


    def remove_inventory_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name] -= quantity
        else:
            return False


    def check_inventory_item(self, item, quantity):
        if self.inventory[item.name] >= quantity:
            return True
        else:
            return False


    def display_inventory(self):
        output = []
        output.append(">>>>>>>>>>{} Item Inventory<<<<<<<<<<\n".format(self.name))
        for item_name, quantity in self.inventory.items():
            output.append("{} - {}\n".format(item_name, quantity))
        output = "".join(output)
        print(output)


class Order(object):

    def __init__(self, store, order_date, buyer, paid=False):
        self.store = store
        self.order_date = order_date
        self.buyer = buyer
        self.order_details = []
        self.paid = paid


    def check_inventory(self, item, quantity):
        return self.store.check_inventory_item(item, quantity)


    def add_order_detail(self, item, quantity):
        if self.check_inventory(item, quantity):
            new_order_detail = OrderDetail(order=self, item=item, quantity=quantity)
            self.order_details.append(new_order_detail)
            self.store.remove_inventory_item(item)
            return True
        else:
            print("ITEM NOT IN INVENTORY")
            return False


    def remove_order_detail(self, order_detail):
        self.order_details.remove(order_detail)


    def total_sale(self):
        sum_total = 0.00
        for order_detail in self.order_details:
            sum_total += order_detail.extended_price()
        return sum_total

    def display_order(self):
        output = []
        output.append(">>>>>>>>>>{} Order<<<<<<<<<<\n".format(self.store.name))
        output.append("Buyer - {}\n".format(self.buyer.name))
        output.append("Order Detail:\n".format(self.buyer.name))
        row_number = 1
        for order_detail in self.order_details:
            line_item = order_detail.item.name
            line_quantity = order_detail.quantity
            line_price = order_detail.item.price
            line_ext_price = order_detail.extended_price()
            output.append("     {}. {}     {}     ${:,.2f}     ${:,.2f}\n".format(
                row_number, line_item, line_quantity, line_price, line_ext_price))
            row_number += 1
        output = "".join(output)
        print(output)


class OrderDetail(object):

    def __init__(self, order, item, quantity):
        self.order = order
        self.item = item
        self.quantity = quantity


    def extended_price(self):
        return self.item.price * self.quantity


class Item(object):

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Buyer(object):

    def __init__(self, id, name, shipping_address):
        self.id = id
        self.name = name
        self.shipping_address = shipping_address
        

class Address(object):
    
    def __init__(self, name, type, street, city, state, zip):
        self.name = name
        self.type = type
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip


sam_address = Address(name="Sam's Home",
                      type="shipping",
                      street="123 Main St",
                      city="Portland",
                      state="OR",
                      zip="97209"
                      )
sam = Buyer(id="1",
            name="Sam",
            shipping_address=sam_address
            )

store_address = Address(name="Sam's Home",
                      type="shipping",
                      street="123 Main St",
                      city="Portland",
                      state="OR",
                      zip="97209"
                      )
store = Store(name="Farmy Farm",
              address=store_address
              )
csa_basket_1 = Item(name="CSA Basket Small",
                    description="Small CSA Basket",
                    price=100.00
                    )
csa_basket_2 = Item(name="CSA Basket Medium",
                    description="Medium CSA Basket",
                    price=150.00
                    )
csa_basket_3 = Item(name="CSA Basket Large",
                    description="Large CSA Basket",
                    price=200.00
                    )

store.add_inventory_item(csa_basket_1)
store.add_inventory_item(csa_basket_2, 2)
store.add_inventory_item(csa_basket_3)

new_order = Order(order_date=1,
                  buyer=sam,
                  store=store
                  )

store.display_inventory()

new_order.add_order_detail(csa_basket_1, 1)
new_order.add_order_detail(csa_basket_2, 1)
new_order.add_order_detail(csa_basket_3, 1)

new_order.display_order()

store.display_inventory()

# print("Total Sale = ${:,.2f}".format(new_order.total_sale()))
