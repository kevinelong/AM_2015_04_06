__author__ = 'LettaRaven'

Structure

# The idea is that one could go to a tab that held situations, ie 'anger/violence' or 'age regression' and kick back
# 5-7 phrases that are most likely to change the situation. For example, if you clicked 'fear/sadness', a response might
# be "Would you like me to hold your hand?". In this way we can provide some immediate relief
# for caregivers rather than just giving them an app of resources for the future.

# Notes: For instance, if an older man becomes upset because he cannot find his mother, an effective response might be:
# 'I know you miss your mother very much, and she loves you too.' Or "Why don’t you tell me all about that time...
# (choose a happy memory.)

# “Say yes AND …”

class User(object):
    { "name"
    'id' }

class situation(): #question, what do I say when....
    { catagories
    'id'
    "name" }

class choice(): #anger/violence, age_regression, fear/sadness
    { "name",
      'id'}

class answer(): #calming, playing, safety
