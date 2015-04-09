

class Recipe(object):
    def __init__(self, name_of_recipe):
        self.name_of_recipe = name_of_recipe
        self.ingredients = IngredientList()
        self.steps = StepList()

    def render(self):
        output = []
        output.append(self.name_of_recipe)
        output.append(self.ingredients.render())
        output.append(self.steps.render())
        return "\n<br>\n".join(output)

class RecipePartList(list):
    def render(self):
        output = []
        for i in self:
            output.append(i.render())
        return "<br>\n".join(output)

class IngredientList(RecipePartList):
    pass

class StepList(RecipePartList):
    pass

class RecipeIngredient(object):
    template = "     -  %s %s of %s"

    def __init__(self, amount, measure, ingredient):
        self.amount = amount
        self.measure = measure
        self.ingredient = ingredient

    def render(self):
        # output = []
        # output.append(str(self.amount))
        # output.append(self.measure.name)
        # output.append(self.ingredient.name)
        #return " ".join(output)
        return self.template % (str(self.amount), self.measure.name, self.ingredient.name)


class RecipeStep(object):
    def __init__(self, step_description):
        self.step_description = step_description

    def render(self):
        return self.step_description


class Ingredient(object):
    def __init__(self, name):
        self.name = name


class Measure(object):
    def __init__(self, name):
        self.name = name


measures = [
    Measure("teaspoon"),
    Measure("cup")
]

kitchen_ingredients = {
    "FLR": Ingredient("flour"),
    "SGR": Ingredient("sugar"),
    "CCO": Ingredient("cocoa")
}

cake = Recipe("flourless chocolate cake")

cake.ingredients.append(
    RecipeIngredient(2.5, measures[1], kitchen_ingredients["SGR"])
)
cake.ingredients.append(
    RecipeIngredient(1.5, measures[1], kitchen_ingredients["CCO"])
)
cake.steps.append(RecipeStep("Mix ingredients together."))

print cake.render()