__author__ = 'LettaRaven'

class Recipe(object):
    def __init__(self, name_of_recipe):
        self.name_of_recipe = name_of_recipe
        self.recipe_ingredients = []
        self.recipe_steps = []

    def __str__(self):
         output = []
         output.append(self.name_of_recipe)
         output.append(self.orderedList(self.recipe_ingredients))
         output.append(self.orderedList(self.recipe_steps))
         return "\n<br>\n".join(output)

    def orderedList(self, collection):
         output = []
         index = 1
         for item in collection:
             output.append(str(index) + ".-" + item.__str__())
             index += 1
         return "<br>\n".join(output)+ "<br>\n"

class RecipeIngredient():
    def __init__(self, amount, measure, ingredient):
        self.amount = amount
        self.measure = measure
        self.ingredient = ingredient

    def __str__(self):
        output = []
        output.append(str(self.amount))
        output.append(self.measure)
        output.append(self.ingredient)
        return " ".join(output)

class Step():
    def __init__(self, line):
        self.line = line
    def __str__(self):
        return self.line

pie = Recipe("Impossible Pie")

pie.recipe_ingredients = [
    RecipeIngredient(0.5, "cups", "flour"),
    RecipeIngredient(1, "cup", "sugar"),
    RecipeIngredient(0.75, "cup", "coconut"),
    RecipeIngredient(4, "each", "eggs"),
    RecipeIngredient(2, "teaspoons", "vanilla"),
    RecipeIngredient(0.5, "cups", "melted butter"),
    RecipeIngredient(0.5, "cups", "hazelnuts"),
    RecipeIngredient(1, "cup", "milk")
]

pie.recipe_steps = [
   Step("Preheat oven to 350 F."),
   Step("Grease tart pan, set aside."),
   Step("Combine first six ingredients in bowl."),
   Step("Mix thoroughly."),
   Step("Add hazelnuts."),
   Step("Slowly add milk until just combined."),
   Step("Pour into prepped pan. Bake 30-35."),
   Step("Take out of oven and allow to cool."),
]

print pie