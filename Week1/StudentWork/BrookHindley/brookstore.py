__author__ = 'coder'

class Store("Widgetland"):
    def __init__ (self, name)
        self.name = Store
            print Store

class Product("Widget"):
    def __init__(self, product, quantity):
        self.product = []
        self.quantity = []

class ProductSearch():

def __init__(self, productSearch, searchResults, selectItem):
    self.productSearch = search
    self.searchResults = search results
    self.selectItem = select item

class Buyer():
    'Common base class for all buyers'
    buyerCount = []

def __init__(self, name, address):
    self.name = buyer
    self.address = address

class Cart():
    "Common base class for buyer cart"
    buyerCart = []

def __init__(self, add, remove, purchase):
    self.add = add to cart
    self.remove = remove frm cart
    self.purchase = purchase

class Order():
    def __init__(self, order, orderNumber):
        self.order = order
        self.ordernumber = orderNumber

class Checkout():
  def __init__(self, total, purchase)
        self.total = confirm total
        self.purchase = checkout



store = Store("amazon")

item = Item("PC Game Programming Explorer", 39.99)
store.products.append(item)

buyer = Buyer("kevin")
store.customers.append(buyer)

line = Line(2, store.products[0])
buyer.cart.lines.append(line)

print(buyer.cart.total())


   # class Employee:
   # 'Common base class for all employees'
   # empCount = 0
   #
   # def __init__(self, name, salary):
   #    self.name = name
   #    self.salary = salary
   #    Employee.empCount += 1
   #
   # def displayCount(self):
   #   print "Total Employee %d" % Employee.empCount
   #
   # def displayEmployee(self):
   #    print "Name : ", self.name,  ", Salary: ", self.salary

# AN EXERCISE IN APPLYING OBJECT ORIENTED DESIGN - A Shopping Cart
# ===
# Create a simple shopping cart application that allows a customer to visit a store, select products, and check out.
# What is the minimal viable product?
#
# Questions to ask when beginning any project:
# ---
# -	What are the things/nouns (Store, Customer, Cart, Item, UI)?
# 	receipt?
#
# -	What are the relationships “is-a”, “has-a”?
#
# 	customer has-a cart
# 	item has-a price
# 	receipt has-a totalPrice
#
# -	What are the actions/verbs that are our methods/functions?
#
# addItem (to cart), removeItem (from cart)
# checkOut, pay,
#
# -	What is general and can be put into a class?
# 	Cart
#
# -	What is specific to each instance and should be passed into each?
# 	Items
#
# -	How can we separate the User Interaction from the classes?
#
# Bonus Shopping Cart Questions:
# ---
# -	How can we get the total in cart?
#
# -	How can we print an itemized receipt?
#
# -	How can we setPosition the Classes into a module?
# 	-put the Classes in a separate file, then import them to the main script with the import statement.
# -	What is the right blend between complex classes vs simple lists and dicts?
#
# Thinking Visually
# ---
# Use Boxes/Circles and Lines/Arrows to diagram your Classes and their relationships.
# Search google for “UML Class Diagram”, and “ERD” for inspirational images.
#
# Vocabulary Building
# ---
# UML Universal Modeling Language - Class Diagram
# ERD Entity Relationship Diagram
#
# Both in Python and elsewhere a List of Dict objects is a common data structure.
# Here is what they are be called in various other languages and contexts:
#
# JavaScript:		Array of Objects
# Databases/ORMs:	Model, Entity, Table or RecordSet
# C:			An Array of Structs