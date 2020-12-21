# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################

# Build a map of allergens to ingredients that cause them
allergen_ingredient_map = {}
for line in input_lines:
  ingredients = line.split(" (")[0].split(" ")
  allergens = line.split("contains ")[1].split(")")[0].split(", ")
  #print(ingredients)
  #print(allergens)

  for allergen in allergens:

    # first time encountering this allergen, put all the ingredients as possible culprits
    if allergen not in allergen_ingredient_map:
      allergen_ingredient_map[allergen] = set()
      for ingredient in ingredients:
        allergen_ingredient_map[allergen].add(ingredient)

    # another food item has this allergen, cross out things that can't be allergens
    map_copy = allergen_ingredient_map[allergen].copy() # copy so we can safely iterate
    for candidate in allergen_ingredient_map[allergen]:
      if candidate not in ingredients:
        map_copy.remove(candidate)
    allergen_ingredient_map[allergen] = map_copy

# simplify allergen_ingredient_map
for doesntmatter in allergen_ingredient_map:
  for x in allergen_ingredient_map:
    if len(allergen_ingredient_map[x]) == 1:
      # remove this from all the other allergen possibilities
      single_allergen = next(iter(allergen_ingredient_map[x]))
      for y in allergen_ingredient_map:
        if x != y:
          if single_allergen in allergen_ingredient_map[y]:
            allergen_ingredient_map[y].remove(single_allergen)

print("Allergen to ingredient mapping:")
print(allergen_ingredient_map)

# built a set of the clean ingredients
clean_ingredients = set()
for line in input_lines:
  ingredients = line.split(" (")[0].split(" ")
  for ingredient in ingredients:
    clean_ingredients.add(ingredient)

for x in allergen_ingredient_map:
  single_allergen = next(iter(allergen_ingredient_map[x]))
  if single_allergen in clean_ingredients:
    clean_ingredients.remove(single_allergen)

print("These ingredients have no allergens:")
print(clean_ingredients)

# count the number of occurrences
count = 0
for line in input_lines:
  ingredients = line.split(" (")[0].split(" ")
  for ingredient in ingredients:
    if ingredient in clean_ingredients:
      count += 1

print("Part 1:")
print(count)

# Part 2 #################################

alphabetize = []
for allergen in allergen_ingredient_map:
  alphabetize.append(allergen)
alphabetize.sort()
print(alphabetize)

canonical = ""
for x in alphabetize:
  canonical = canonical + "," + next(iter(allergen_ingredient_map[x]))

print(canonical[1:])
