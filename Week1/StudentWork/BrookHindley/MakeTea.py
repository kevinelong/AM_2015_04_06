# Tea Kettle

def kettle ();
    # this is the kettle to be filled with water

def faucet ();
    # faucet to be used to fill kettle

def burner ();
    # this is the stove burner used to heat the water

def mug();
    # this is the mug the user will pour the tea into

def tea([1 "Decaf" : 2 "Caf"]);
        [ G "Ginseng" : E "Earl Grey"])
    print "Type 1 for decaf and type 2 for caf";
    print "Type G for Ginseng and E for Earl Gray"
    # types of tea (decaf or caf)

def steeptminutes();
    print "How many minutes do you want to steep for? Type 4 for four minutes and 6 for six minutes";
     # number of minutes the user wants tea to steep

def run_faucet[C "Cold" : H "Hot"];
    # user runs the faucet

if run_faucet[H]
    print "You must use cold water to make tea, dummy!"
    #user runs faucet in hot triggering error message

if run_faucet[C]
    print "Don't let the kettle overflow!"
    #user runs Cold faucet triggering reminder to not overfill













# make tea
#
# kettle .. microwave
# water
#     goal temp
#     Qty
#
# Tea
#     Qty
#     preferred type
#     steep time minutes
#
# Steps:
#
# 1. fill kettle
#     if kitchen
#         a. Go to sink
#         b. turn on cold water
#         c. place kettle below the faucet
#         while kettle not full
#         wait
#         if water full break
#         Remove kettle
#             turn off water
#                 turn off stove
#
# 2. Place kettle on stove
#     turn on burner (which)
# while not at goal temp wait
#
#     public method (make tea)

# milk? sugar? lemon?
#
# (type [] ) sugarlumps 0-N

# Board Game
#
# tic tac toe
# classes = board (rows) game pieces x type o type blank (presence or absense of a piece)
# players would have a name property (ordinal property e.g. player 1 or 2 or color)
# 1. build or clear board
# 2. Notify player it's their turn'
# 3. Give first player pieces of type x
# 4. Get input from player (which row, column they want to place in)

