# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE
class Model(object):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = []

    def create(self, item):
        self.objects.append(item)

    def retrieve(self, field_name, field_value):
        for object in self.objects:
            if object[field_name] == field_value:
                return object


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

# define models (
app.models["user"] = Model("user", ["name", "score"])
app.models["game"] = Model("game", ["game_name", "description"])

# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": "9"},
    {"name": "Carol", "score": "11"},
    {"name": "Ted", "score": "15"},
    {"name": "Alice", "score": "13"}]

app.models["game"].create({"game_name": "marbles", "description": "toss your marbles"})

app.models["game_instance"] = Model("game_instance", ["date", "time_played"])
app.models["game_instance"].create({
    "date": "Today",
    "time_played": "1 hour"
})

score_template = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
scores_view = View(score_template, app.models["user"])

game_play_template = "\n<h4>{{date}}, you played for <strong>{{time_played}}</strong>.</h4><br>\n"
game_play_view = View(game_play_template, app.models["game_instance"])

app.controller.routes = {
    "/scores/": scores_view,
    "/score/": scores_view,
    "/gameplay/": game_play_view
}

request_path = "/gameplay/"
html_output = app.controller.route(request_path)
with open("output.html", "width") as f:
    f.write(html_output)
