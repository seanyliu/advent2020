import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import helpers

class Bag:

  def __init__(self, bag_type, rules):
    self.bag_type = bag_type
    self.rules = rules
    self.contains = {}

  def get_type(self):
    return self.bag_type

  def add_contains(self, bag_type, quantity):
    self.contains[bag_type] = quantity

  def get_contains(self):
    return self.contains

  def is_container_of(self, is_container_of_type):
    for bag_type in self.contains:
      if bag_type == is_container_of_type:
        return True
      if rules[bag_type].is_container_of(is_container_of_type):
        return True
    return False

  def count_bags_inside(self):
    count = 0
    if (self.contains):
      for bag_type in self.contains:
        count += int(self.contains[bag_type])
        count += int(self.contains[bag_type]) * rules[bag_type].count_bags_inside()
    return count


rules = {}

input_lines = helpers.read_lines_from_file('input.txt')
for line in input_lines:
  holder_type = line.split("contain")[0].split("bags")[0].strip()
  inside_bags = line.split("contain")[1].strip().split(",")
  b = Bag(holder_type, rules)
  rules[holder_type] = b
  for inside in inside_bags:
    inside = inside.strip()
    inside = inside.split("bag")[0].strip() # trim "bags."

    # get quantity of bag type
    quantity = inside.split(" ")[0]
    inside_type = " ".join(inside.split(" ")[1:])
    if quantity != "no":
      b.add_contains(inside_type, quantity)

# print rules
count_shiny_gold_containers = 0
for rule in rules:
  if rules[rule].is_container_of("shiny gold"):
    count_shiny_gold_containers += 1

print(count_shiny_gold_containers)

print(rules["shiny gold"].count_bags_inside())
