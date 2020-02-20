#!/usr/bin/python

import math

recipe = {'milk': 100, 'butter': 50, 'flour': 5}
ingredients = {'milk': 132, 'butter': 48, 'flour': 51}


def recipe_batches(recipe, ingredients):
    cache = []
    if recipe.keys() != ingredients.keys():
        return 0
    for i in recipe.keys():
        cache.append(math.floor(ingredients[i]/recipe[i]))
    return min(cache)


recipe_batches(recipe, ingredients)
if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
