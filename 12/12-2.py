# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

class Waypoint:
  def __init__(self):
    self.reset()

  def reset(self):
    # starts 10 east and 1 north relative to ship
    self.rel_x = 10
    self.rel_y = -1

  def move_units(self, x, y):
    self.rel_x += x
    self.rel_y += y

  def rotate(self, angle):

    # flip y axis to be negative
    curr_angle = self.get_curr_angle()

    distance = math.sqrt(math.pow(self.rel_x,2) + math.pow(self.rel_y,2))
    self.rel_x = distance * math.cos(math.radians(curr_angle + angle))
    self.rel_y = -distance * math.sin(math.radians(curr_angle + angle))

  def get_curr_angle(self):
    curr_angle = math.degrees(math.atan(-self.rel_y/self.rel_x))
    if self.rel_x < 0:
      curr_angle += 180
    return curr_angle





class Ship:
  def __init__(self):
    self.reset()

  def reset(self):
    self.x = 0
    self.y = 0
    self.facing = 0 # degrees
    self.waypoint = Waypoint()

  def move_direction(self, direction, units):
    if direction == "N":
      self.waypoint.move_units(0, -units)
    elif direction == "S":
      self.waypoint.move_units(0, units)
    elif direction == "E":
      self.waypoint.move_units(units, 0)
    elif direction == "W":
      self.waypoint.move_units(-units, 0)
    elif direction == "L":
      self.waypoint.rotate(units)
    elif direction == "R":
      self.waypoint.rotate(-units)
    elif direction == "F":
      # note that north is negative and south is positive, so the y axis is flipped
      #self.move_units(units*math.cos(math.radians(self.facing)), -units*math.sin(math.radians(self.facing)))
      self.x += self.waypoint.rel_x * units
      self.y += self.waypoint.rel_y * units

  def get_manhattan_distance(self):
    return abs(self.x) + abs(self.y)

  def move_units(self, x, y):
    self.x += x
    self.y += y

  def print_state(self):
    print("waypoint ("+str(self.waypoint.rel_x)+", "+str(self.waypoint.rel_y)+")")
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
