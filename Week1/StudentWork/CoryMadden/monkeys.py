__author__ = 'Cory'

def monkey_trouble(a_smile, b_smile):
    if( a_smile == True and b_smile == True ):
        print "Ruh roh, we're in trouble!"
    elif( a_smile == False and b_smile == False):
        print "Ruh roh, we're in trouble!"
    else:
        print "All good in the hood..."

monkey_trouble(True,True)
monkey_trouble(True,False)
monkey_trouble(False,False)