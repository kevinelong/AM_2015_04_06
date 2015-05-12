__author__ = 'LettaRaven'

Structure

# The idea is that one could go to a tab that held situations, ie 'anger/violence' or 'age regression' and kick back
# 3-5 phrases that are most likely to change the situation. For example, if you clicked 'fear/sadness', a response might
# be "Would you like me to hold your hand?". In this way we can provide some immediate relief
# for caregivers rather than just giving them an app of resources for the future.

# Notes: For instance, if an older man becomes upset because he cannot find his mother, an effective response might be:
# 'I know you miss your mother very much, and she loves you too.' If they are focusing on something negative, you might
# say "Why don’t you tell me all about that time... (choose a happy memory from their past.) * You can also choose to
# remind and compliment them on something they did that was brave or impacted you. Example: to a disabled patient who has
# lived a life they never expected you could say 'You were very courageous to ignore those who said you couldn't do it.'

# “Say yes AND …”

class User(object):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.Textfield()

class Behavior(): # question, what do I say when....
 #    (categories: anger/violence, age_regression, fear/sadness)
    Behavior_text = models.CharField(max_length=200)
 { 'id'
    "name" }

class ResponseOption(): # anger/violence, age_regression, fear/sadness
    ResponseOption = models.choice_text
    def __str__(self):

class IdealResponse(): # calming, playing, safety
    IdeaReponse = models.choice_text