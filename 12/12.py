# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################
class Ship:
  def __init__(self):
    self.reset()

  def reset(self):
    self.x = 0
    self.y = 0
    self.facing = 0 # degrees

  def move_direction(self, direction, units):
    if direction == "N":
      self.move_units(0, -units)
    elif direction == "S":
      self.move_units(0, units)
    elif direction == "E":
      self.move_units(units, 0)
    elif direction == "W":
      self.move_units(-units, 0)
    elif direction == "L":
      self.facing += units
    elif direction == "R":
      self.facing -= units
    elif direction == "F":
      self.move_units(units*math.cos(math.radians(self.facing)), -units*math.sin(math.radians(self.facing)))

  def get_manhattan_distance(self):
    return abs(self.x) + abs(self.y)

  def move_units(self, x, y):
    self.x += x
    self.y += y

  def print_state(self):
    print("location ("+str(self.x)+", "+str(self.y)+"), facing "+str(self.facing))



# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
s = Ship()
for line in input_lines:
  direction = line[0]
  units = int(line[1:])
  s.move_direction(direction, units)
  s.print_state()

print(s.get_manhattan_distance())

# Part 2 #################################
