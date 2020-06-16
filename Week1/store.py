# AN EXERCISE IN APPLYING OBJECT ORIENTED DESIGN - A Shopping Cart
# ===
# Create a simple shopping cart application that allows a customer to
# make a purchase.
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
