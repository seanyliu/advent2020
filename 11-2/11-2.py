# regular imports ########################
import math
import copy
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################
def run(input_grid):
  grid = copy.deepcopy(input_grid)
  for x in input_grid:
    for y in input_grid[x]:
      if input_grid[x][y] == "L":
        if should_flip_l(x, y, input_grid):
          grid[x][y] = "#"
      elif input_grid[x][y] == "#":
        # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        if should_flip_pound(x, y, input_grid):
          grid[x][y] = "L"
  return grid

def is_seat_occupied_up(x, y, grid):
  i = y
  i -= 1
  while i in grid[x]:
    seat = grid[x][i]
    if seat == "#":
      return True
    elif seat == "L":
      return False
    else:
      i -= 1
  return False

def is_seat_occupied_down(x, y, grid):
  i = y
  i += 1
  while i in grid[x]:
    seat = grid[x][i]
    if seat == "#":
      return True
    elif seat == "L":
      return False
    else:
      i += 1
  return False

def is_seat_occupied_left(x, y, grid):
  i = x
  i -= 1
  while i in grid:
    seat = grid[i][y]
    if seat == "#":
      return True
    elif seat == "L":
      return False
    else:
      i -= 1
  return False

def is_seat_occupied_right(x, y, grid):
  i = x
  i += 1
  while i in grid:
    seat = grid[i][y]
    if seat == "#":
      return True
    elif seat == "L":
      return False
    else:
      i += 1
  return False

def is_seat_occupied_tl(x, y, grid):
  i = x-1
  j = y-1
  while i in grid and j in grid[i]:
    seat = grid[i][j]
    if seat == "#":
      return True
    elif seat == "L":
      return False
    else:
      i -= 1
      j -= 1
  return False

def is_seat_occupied_tr(x, y, grid):
  i = x+1
  j = y-1
  while i in grid and j in grid[i]:
    seat = grid[i][j]
    if seat == "#":
      return True
    elif seat == "L":
      return False
    else:
      i += 1
      j -= 1
  return False

def is_seat_occupied_bl(x, y, grid):
  i = x-1
  j = y+1
  while i in grid and j in grid[i]:
    seat = grid[i][j]
    if seat == "#":
      return True
    elif seat == "L":
      return False
    else:
      i -= 1
      j += 1
  return False

def is_seat_occupied_br(x, y, grid):
  i = x+1
  j = y+1
  while i in grid and j in grid[i]:
    seat = grid[i][j]
    if seat == "#":
      return True
    elif seat == "L":
      return False
    else:
      i += 1
      j += 1
  return False


def should_flip_l(x, y, grid):
  # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.

  # cardinal
  if is_seat_occupied_up(x, y, grid):
    return False
  if is_seat_occupied_down(x, y, grid):
    return False
  if is_seat_occupied_left(x, y, grid):
    return False
  if is_seat_occupied_right(x, y, grid):
    return False
  
  # diagonals
  if is_seat_occupied_tl(x, y, grid):
    return False
  if is_seat_occupied_tr(x, y, grid):
    return False
  if is_seat_occupied_bl(x, y, grid):
    return False
  if is_seat_occupied_br(x, y, grid):
    return False

  return True

def should_flip_pound(x, y, grid):
  # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
  adjacent_occupied = 0

# cardinal
  if is_seat_occupied_up(x, y, grid):
    adjacent_occupied += 1
  if is_seat_occupied_down(x, y, grid):
    adjacent_occupied += 1
  if is_seat_occupied_left(x, y, grid):
    adjacent_occupied += 1
  if is_seat_occupied_right(x, y, grid):
    adjacent_occupied += 1
  
  # diagonals
  if is_seat_occupied_tl(x, y, grid):
    adjacent_occupied += 1
  if is_seat_occupied_tr(x, y, grid):
    adjacent_occupied += 1
  if is_seat_occupied_bl(x, y, grid):
    adjacent_occupied += 1
  if is_seat_occupied_br(x, y, grid):
    adjacent_occupied += 1

  if adjacent_occupied >= 5:
    return True
  else:
    return False

def is_grid_equal(grid_a, grid_b):
  for x in grid_a:
    for y in grid_a[x]:
      if grid_a[x][y] != grid_b[x][y]:
        return False
  return True

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 2 #################################
grid = helpers.get_grid_from_lines(input_lines)

runcount = 0
while True:
  nextgrid = run(grid)
  runcount += 1
  if is_grid_equal(nextgrid, grid):
    print("grids equal each other after "+str(runcount)+" rounds")
    occupied_count = 0
    for x in nextgrid:
      for y in nextgrid[x]:
        if nextgrid[x][y] == "#":
          occupied_count += 1
    print(str(occupied_count)+" seats occupied")
    break
  else:
    grid = nextgrid
