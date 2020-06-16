# Making Tea

#Below are the classes needed for the user to make tea

class Kettle:
    def __init__(self, water, cold, hot):
        self.water.cold = cold
        self.water.hot = hot
    # this is the kettle to be filled with water

class Faucet:
    def __init__(self, faucet, on, off):
        self.on = faucet on
        self.off = faucet off
    # faucet to be used to fill kettle

class Faucettemp:
    def __init__(self, faucetemp, cold, hot):
        self.cold = cold water
        self.hot = hot water

class Burner:
    def __init__(self, on, off):
        self.on = on
        self.off = off
    # this is the stove burner used to heat the water

class Mug:
    def __init__(self, full, empty):
        self.full = full
        self.empty = empty
    # this is the mug the user will pour the tea into

class TeaType:
    def __init__(self, decaf, caf):
        self.decaf = decaf
        self.caf = caf
    # user selects whether they want decaf or caf tea

class Teaflavor:
    def __init__(self, gingseng, earlgray):
        self.ginseng = ginseng
        self.Earl = earl Gray
    # types of tea (decaf or caf)

class Steepminutes:
    def __init__(self, four, six):
        self.four = 4 minute steep
        self.six = 6 minute steep
     # number of minutes the user wants tea to steep

if self.faucet.hot:
    print "You must use cold water to make tea, dummy!"
    #user runs faucet in hot triggering error message

if self.faucet.cold:
    print "Don't let the kettle overflow!"
    #user runs Cold faucet triggering reminder to not overfill

#Below are the functions needed to actually make the tea

def MakeTea if (
    self.faucet.on :
    self.water.cold :
    self.teatype.decaf == self.teatype.caf :
    self.teaflavor.g == self.teaflavor.e
    self.steepminutes.4 == self.steepminutes6 :
    print "You have just made a cup of %teatype %teaflavor tea which %steepminutes. Enjoy!"


)





# def {tea(1) and teaflavor(G) and run_faucet(C) and burner(0) and burner(f) and steepminutes(6)};
#     print "Your decaf cup of Ginseng tea has been steeped for 6-minutes and is now ready!"













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

