__author__ = 'Cory'


class Model():
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = []

    def create(self, item):
        self.objects.append(item)


class View():
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


class Controller():
    def __init__(self):
        self.routes = {}

    def route(self, path):
        return self.routes[path].render()


class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.Controller = Controller()


app = Application()


class address():
    def __init__(self):
        self.line1 = "1717 SW Park Ave"
        self.line2 = "#1412"
        self.city = "Portland"
        self.state = "OR"
        self.zip_code = 97201

    def print_address(self):
        print self.__init__


app.models["Products"] = Model("Products", ["name", "price", "weight"])
app.models["User"] = Model("User", ["name", "address", "email"])

app.models["Products"].objects = [
    {"name": "Shoes", "price": 80, "weight": 10},
    {"name": "Hat", "price": 25, "weight": 2},
    {"name": "Coffee Maker", "price": 40, "weight": 10}
]
Bob = address()
Carol = address()

app.models["User"].objects = [
    {"name": "Bob", "address": "address", "email": "bob@email.com"},
    {"name": "Carol", "address": "address"},
    {"name": "Alice", "email": "Alice@wonderland.com"}
]

app.Controller.routes = {
    "/users/": View("\nUsername is: {{name}}, address is: {{address}}, and email is: {{email}}\n", app.models["User"]),
    "/Products/": View("\nProduct name: {{name}}\nProduct Price: {{price}}\nWeight: {{weight}}\n",app.models["Products"])
}

request_path = "/users/"
p = "/Products/"

print(app.Controller.route(request_path))
print app.Controller.route(p)