# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers
import re

# functions ##############################
class Hex:
  def __init__(self, x, y):
    # x and y represent the centers of the hexagon
    self.x = x
    self.y = y
    self.color = "white"

    # https://www.redblobgames.com/grids/hexagons/
    # e:  x+2, y
    # se: x+1, y+3
    # sw: x-1, y+3
    # w:  x-2, y
    # nw: x-1, y-3
    # ne: x+1, y-3

  def print(self):
    return "("+str(self.x)+", "+str(self.y)+")"

  def e(self, create_tile=True):
    return get_hex_from_grid(self.x+2, self.y, grid, create_tile)

  def se(self, create_tile=True):
    return get_hex_from_grid(self.x+1, self.y+3, grid, create_tile)

  def sw(self, create_tile=True):
    return get_hex_from_grid(self.x-1, self.y+3, grid, create_tile)

  def w(self, create_tile=True):
    return get_hex_from_grid(self.x-2, self.y, grid, create_tile)

  def nw(self, create_tile=True):
    return get_hex_from_grid(self.x-1, self.y-3, grid, create_tile)

  def ne(self, create_tile=True):
    return get_hex_from_grid(self.x+1, self.y-3, grid, create_tile)

  def count_black_neighbors(self, create_tile=True):
    count = 0
    if self.e(create_tile) and self.e().color == "black":
      count += 1
    if self.se(create_tile) and self.se().color == "black":
      count += 1
    if self.sw(create_tile) and self.sw().color == "black":
      count += 1
    if self.w(create_tile) and self.w().color == "black":
      count += 1
    if self.nw(create_tile) and self.nw().color == "black":
      count += 1
    if self.ne(create_tile) and self.ne().color == "black":
      count += 1
    return count

def get_hex_by_identifier(identifiers, grid):
  x = 0
  y = 0
  while len(identifiers) > 0:
    if identifiers.startswith("e"):
      #print("e")
      identifiers = identifiers[1:]
      x = x + 2
      y = y
    elif identifiers.startswith("se"):
      #print("se")
      identifiers = identifiers[2:]
      x = x + 1
      y = y + 3
    elif identifiers.startswith("sw"):
      #print("sw")
      identifiers = identifiers[2:]
      x = x - 1
      y = y + 3
    elif identifiers.startswith("w"):
      #print("w")
      identifiers = identifiers[1:]
      x = x - 2
      y = y
    elif identifiers.startswith("nw"):
      #print("nw")
      identifiers = identifiers[2:]
      x = x - 1
      y = y - 3
    elif identifiers.startswith("ne"):
      #print("ne")
      identifiers = identifiers[2:]
      x = x + 1
      y = y - 3
    else:
      print("ERROR")
      break
  return get_hex_from_grid(x, y, grid)

def get_hex_from_grid(x, y, grid, create_tile=True):
  if x not in grid:
    if not create_tile:
      return None
    grid[x] = {}
  if y not in grid[x] or not grid[x][y]:
    if not create_tile:
      return None
    grid[x][y] = Hex(x, y)
  return grid[x][y]

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
grid = {}
grid[0] = {}
grid[0][0] = Hex(0, 0)

for line in input_lines:
  h = get_hex_by_identifier(line, grid)
  if h.color == "white":
    h.color = "black"
  else:
    h.color = "white"

def count_black(grid):
  black_count = 0
  for x in grid:
    for y in grid[x]:
      if grid[x][y] and grid[x][y].color == "black":
        black_count += 1
  return black_count

print("Part 1: "+str(count_black(grid)))

# Part 2 #################################

def conway(grid):
  grid_counter = copy_grid(grid)
  for x in grid_counter:
    for y in grid_counter[x]:
      if grid_counter[x][y]:
        # has the added effect of expanding the grid
        grid_counter[x][y] = grid_counter[x][y].count_black_neighbors()

  for x in grid_counter:
    for y in grid_counter[x]:
      if grid[x][y]:
        if grid[x][y].color == "black":
          if grid_counter[x][y] == 0 or grid_counter[x][y] > 2:
            grid[x][y].color = "white"
        elif grid[x][y].color == "white":
          if grid_counter[x][y] == 2:
            grid[x][y].color = "black"
        else:
          print("ERROR")

  reduce_grid(grid)

def count_all(grid):
  count = 0
  for x in grid:
    for y in grid[x]:
      if grid[x][y]:
        count += 1
  return count

def copy_grid(grid):
  copy = {}
  for x in grid:
    for y in grid[x]:
      helpers.add_to_grid(x, y, grid[x][y], copy)
  return copy

def reduce_grid(grid):
  grid_counter = copy_grid(grid)
  for x in grid_counter:
    for y in grid_counter[x]:
      if grid[x][y] and grid[x][y].color == "white" and grid[x][y].count_black_neighbors(False) == 0:
        grid[x][y] = None

# first, extend the grid out by 1 tile all around
# count_black_neighbors has the added benefit of doing this
# based on the way we access items!
print(str(count_all(grid)) + " tiles in grid before expansion")
print("Part 1: "+str(count_black(grid)))

# make a copy of the grid
grid_counter = copy_grid(grid)
for x in grid_counter:
  for y in grid_counter[x]:
    if grid_counter[x][y]:
      # has added effect of expanding the grid
      grid[x][y].count_black_neighbors(True)
print(str(count_all(grid)) + " tiles in grid after expansion")
print("Part 1: "+str(count_black(grid)))

reduce_grid(grid)
print(str(count_all(grid)) + " tiles in grid after reduction")
print("Part 1: "+str(count_black(grid)))

for day in range(100):
  conway(grid)
  print("Day "+str(day+1)+": "+str(count_black(grid)))


