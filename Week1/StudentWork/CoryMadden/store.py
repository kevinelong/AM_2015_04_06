__author__ = 'Cory'

item_dict = {1313:{"price":32.50,"name":"Hat","weight":10},
             1212:{"price":100.50,"name":"Shoes","weight":10}}

item_price = 1


class Cart():
    def __init__(self, user):
        self.user_name = user
        self.address = {"line1": "", "line2": "", "city": "", "state": "", "zip": 00000}
        self.cart_list = []
        self.total = 0

    def add_item(self, item_num):
        for item in item_dict:
            if item == item_num:
                self.cart_list.append(item_num)
                self.total += item_dict[item_num]["price"]

    def remove_item(self, item_num):
        for x in self.cart_list:
            if x == item_num:
                for item in item_dict:
                    if item == item_num:
                        self.total -= item_dict[item_num]["price"]
                for item in self.cart_list:
                    if item == item_num:
                        del item



User1 = Cart("C")

User1.add_item(1313)
print User1.total
User1.add_item(1212)
print User1.total
User1.add_item(1313)
User1.add_item(1313)
print User1.cart_list
User1.remove_item(1212)
print User1.total