# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
cups = []
for line in input_lines:
  for char in line:
    cups.append(int(char))

class Game:
  def __init__(self, cups):
    self.current_cup_index = 0
    self.cups = cups
    self.move_count = 1
    pass

  def move(self, debug=False):
    cups = self.cups
    current_cup_index = self.current_cup_index
    current_cup = cups[current_cup_index]

    if debug:
      print("-- move "+str(self.move_count)+" --")
      print("cups: "+str(cups))
      self.move_count += 1

    # remove the 3 cups clockwise of the current cup
    cups_copy = cups.copy()
    removed_cups = []
    for i in range(3):
      remove_index = (cups_copy.index(current_cup) + 1) % len(cups_copy)
      removed_cup = cups_copy.pop(remove_index)
      #print(remove_index)
      #print("Removed: "+str(removed_cup))
      #print(cups_copy)
      removed_cups.append(removed_cup)
    #print("removed cups: "+str(removed_cups))

    # select a destination cup
    destination_cup = cups[current_cup_index] - 1
    max_label = max(cups)
    min_label = min(cups)
    while destination_cup not in cups_copy:
      destination_cup = destination_cup - 1
      if destination_cup < min_label:
        destination_cup = max_label

    if debug:
      print("current cup: "+str(current_cup))
      print("pick up: "+str(removed_cups))
      print("circle: "+str(cups_copy))
      print("destination: "+str(destination_cup))

    # go to the destination
    pos = cups_copy.index(destination_cup) + 1
    for i in range(len(removed_cups)):
      cups_copy.insert(i + pos, removed_cups[i])

    if debug:
      print("Inserted cups: "+str(cups_copy))

    current_cup_index = (cups_copy.index(current_cup) + 1) % len(cups_copy)

    self.current_cup_index = current_cup_index
    self.cups = cups_copy

game = Game(cups)

for i in range(100):
  game.move(False)

print(game.cups)
answer = ""
for i in range(len(game.cups)):
  if i == 0:
    continue
  cup1_index = game.cups.index(1)
  print_index = (cup1_index + i) % len(game.cups)
  answer = answer + str(game.cups[print_index])

print(answer)

# Part 2 #################################
