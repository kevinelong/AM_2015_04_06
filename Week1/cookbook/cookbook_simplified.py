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
            output.append(str(index) + ". - " + item.__str__())
            index += 1
        return "<br>\n".join(output)


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


cake = Recipe("flourless chocolate cake")

cake.recipe_ingredients = [
    RecipeIngredient(2.5, "cups", "sugar"),
    RecipeIngredient(1.5, "tablespoons", "cocoa"),
    RecipeIngredient(2, "sticks", "butter")
]

cake.recipe_steps = [
    "Add dry ingredients to bowl.",
    "Mix thoroughly with whisk."
]

print
cake.getString()