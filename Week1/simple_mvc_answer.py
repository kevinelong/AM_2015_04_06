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
                    item_template = item_template.replace("{{" + field + "}}", str(item[field]))
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
app.models["product"] = Model("product", ["name", "price"])

# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": 9},
    {"name": "Carol", "score": 11},
    {"name": "Ted", "score": 15},
    {"name": "Alice", "score": 13}
]
# We could add another either of these two ways
app.models["user"].create({"name": "Kevin", "score": "22"})
app.models["user"].objects.append({"name": "Kay", "score": "33"})

score_template = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
scores_view = View(score_template, app.models["user"])

#products are a whole new type of model
app.models["product"].objects = [
    {"name": "Banana", "price": 1.45},
    {"name": "Orange", "price": 2.45}
]
product_template = "\nProduct <em>{{name}}</em>, has the price of <strong>{{price}}</strong>.<br>\n"
product_view = View(product_template, app.models["product"])

app.controller.routes = {
    "/scores/": scores_view,
    "/product/": product_view,
}
request_path = "/scores/"
print(app.controller.route(request_path))

f = open("output.html", "w")
f.write(app.controller.route("/product/"))
f.close()