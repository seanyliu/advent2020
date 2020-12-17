# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
grid = {}

def insert_into_grid(x, y, z, w, state, grid):
  if x not in grid:
    grid[x] = {}

  if y not in grid[x]:
    grid[x][y] = {}

  if z not in grid[x][y]:
    grid[x][y][z] = {}

  grid[x][y][z][w] = state

def get_value_from_grid(x, y, z, w, grid):
  if x not in grid:
    return "."

  if y not in grid[x]:
    return "."

  if z not in grid[x][y]:
    return "."

  if w not in grid[x][y][z]:
    return "."

  return grid[x][y][z][w]

#insert_into_grid(0, 0, 0, "#")
#print(grid)
#print(get_value_from_grid(0, 0, 1))

for y in range(len(input_lines)):
  line = input_lines[y]
  for x in range(len(line)):
    insert_into_grid(x, y, 0, 0, line[x], grid)

def print_grid_zw(grid, z, w):
  min_y = min(grid[0].keys())
  max_y = max(grid[0].keys())
  for y in range(min_y, max_y+1):
    line = ""
    min_x = min(grid.keys())
    max_x = max(grid.keys())
    for x in range(min_x, max_x+1):
      #print(str(x) + "," + str(y) + "=" + grid[x][y])
      line = line + get_value_from_grid(x, y, z, w, grid)
    print(line)

#print_grid_zw(grid, 0, 0)

def run(grid):
  next_grid = {}

  min_x = min(grid.keys())
  max_x = max(grid.keys())
  min_y = min(grid[0].keys())
  max_y = max(grid[0].keys())
  min_z = min(grid[0][0].keys())
  max_z = max(grid[0][0].keys())
  min_w = min(grid[0][0][0].keys())
  max_w = max(grid[0][0][0].keys())

  for x in range(min_x-1, max_x+2):
    for y in range(min_y-1, max_y+2):
      for z in range(min_z-1, max_z+2):
        for w in range(min_w-1, max_w+2):

          curr_cube = get_value_from_grid(x, y, z, w, grid)
          count_neighbors = count_active_neighbors(x, y, z, w, grid)

          if curr_cube == "#":
            if count_neighbors == 2 or count_neighbors == 3:
              insert_into_grid(x, y, z, w, "#", next_grid)
            else:
              insert_into_grid(x, y, z, w, ".", next_grid)
          else:
            if count_neighbors == 3:
              insert_into_grid(x, y, z, w, "#", next_grid)
            else:
              insert_into_grid(x, y, z, w, ".", next_grid)

          #print(grid[x][y][z])

  return next_grid

def count_active_neighbors(x, y, z, w, grid):
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      for k in range(-1, 2):
        for l in range (-1, 2):
          if i == 0 and j == 0 and k == 0 and l == 0:
            continue
          #print(str(i)+","+str(j)+","+str(k))
          #print(get_value_from_grid(x+i, y+j, z+k, grid))
          neighbor = get_value_from_grid(x+i, y+j, z+k, w+l, grid)
          if neighbor == "#":
            count += 1
  return count

for i in range(6):
  #print ("Cycle: "+str(i+1))
  grid = run(grid)
  #print("z = -1")
  #print_grid_z(grid, -1)
  #print("z = 0")
  #print_grid_z(grid, 0)
  #print("z = 1")
  #print_grid_z(grid, 1)

def count_actives_in_grid(grid):
  count = 0
  min_x = min(grid.keys())
  max_x = max(grid.keys())
  min_y = min(grid[0].keys())
  max_y = max(grid[0].keys())
  min_z = min(grid[0][0].keys())
  max_z = max(grid[0][0].keys())
  min_w = min(grid[0][0][0].keys())
  max_w = max(grid[0][0][0].keys())
  for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
      for z in range(min_z, max_z+1):
        for w in range(min_w, max_w+1):
          if get_value_from_grid(x, y, z, w, grid) == "#":
            count += 1
  return count

print(count_actives_in_grid(grid))





# Part 2 #################################
