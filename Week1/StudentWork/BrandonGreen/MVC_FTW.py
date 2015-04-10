# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE


class Model(object):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = []

    def create(self, item):
        self.objects.append(item)


# VIEW: A TEMPLATE FOR A PAGE OR PAGE FRAGMENT
class View(object):
    def __init__(self, template, model):
        self.template = template
        self.model = model

    def render(self):
        output = ""
        for item in self.model.objects:
            item_template = self.template
            for field in self.model.fields:
                if field in item.keys():
                    item_template = item_template.replace("{{" + field + "}}", item[field])
            output += item_template
        return output


# CONTROLLER: Routes messages
class Controller(object):
    def __init__(self):
        self.routes = {}

    def route(self, path):
        return self.routes[path].render()


# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()

# CREATE AN APPLICATION INSTANCE
app = Application()

# define models

app.models['players'] = Model('player', ['user_name', 'level', 'acct_type'])
app.models['adventures'] = Model('adventure', ['adventure_name', 'challenge_rating'])

# load model objects form database tables
app.models['players'].objects = [
    {'user_name': 'spacefish', 'level': '9000', 'acct_type': 'Premium'},
    {'user_name': 'redrosid999', 'level': '5', 'acct_type': 'Free'},
    {'user_name': 'brian7ls', 'level': '155', 'acct_type': 'Premium'},
    {'user_name': 'spam_and_eggs_bot', 'level': '1', 'acct_type': 'Trial'}
]

app.models['adventures'].objects = [
    {'adventure_name': 'Treasure Island', 'challenge_rating': '10'},
    {'adventure_name': 'The Direlands', 'challenge_rating': '99'},
    {'adventure_name': 'Sellwood Forest', 'challenge_rating': '1'}
]

# 1. Add a new model, view/template and route)

level_template = "\nHail, {{user_name}}!  Current level: {{level}}  Thanks for playing Adventure {{acct_type}} Edition!\n"

level_view = View(level_template, app.models['players'])

app.controller.routes = {
    '/home/': level_view,
    '/level/': level_view,
    '/character/': level_view
}
# 2. call your new route and write output to a file

request_path = '/home/'

print app.controller.route(request_path)

# 3. open file in your browser


