# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################
class Tile:
  def __init__(self, grid_lines):
    self.reset()
    self.grid = self.set_grid(grid_lines)

  def reset(self):
    self.grid = {}

  def set_grid(self, grid_lines):
    return helpers.get_grid_from_lines(grid_lines)

  def print_grid(self):
    helpers.print_grid(self.grid)

  def transform_flip_x(self):
    self.grid = helpers.transform_flip_x(self.grid)

  def transform_flip_y(self):
    self.grid = helpers.transform_flip_y(self.grid)

  def transform_rotate_90(self):
    self.grid = helpers.transform_rotate_90(self.grid)

  def transform_rotate_180(self):
    self.grid = helpers.transform_rotate_90(self.grid)
    self.grid = helpers.transform_rotate_90(self.grid)

  def transform_rotate_270(self):
    self.grid = helpers.transform_rotate_90(self.grid)
    self.grid = helpers.transform_rotate_90(self.grid)
    self.grid = helpers.transform_rotate_90(self.grid)

# actual code ############################
input_lines = helpers.read_lines_from_file('input-mark.txt')

# Part 1 #################################

# generate a dictionary of the tiles_lines
tiles_lines_dict = {}
tile_name = ""
tile_lines = []
for i in range(len(input_lines)):
  line = input_lines[i]
  if line.split(" ")[0] == "Tile":
    tile_name = line.split(" ")[1].split(":")[0]
  elif line == "":
    tiles_lines_dict[tile_name] = tile_lines
    tile_lines = []
  else:
    tile_lines.append(line)

  if i == len(input_lines)-1:
    tiles_lines_dict[tile_name] = tile_lines
    tile_lines = []

# generate tile objects
tiles_dict = {}
for tile_name in tiles_lines_dict:
  tile = Tile(tiles_lines_dict[tile_name])
  tiles_dict[tile_name] = tile

# debug
"""
for tile_name in tiles_dict:
  print(tile_name)
  tiles_dict[tile_name].print_grid()

print("2311")
tiles_dict["2311"].print_grid()

print("transform_rotate_270")
tiles_dict["2311"].transform_rotate_270()
tiles_dict["2311"].print_grid()
"""

class Board:
  def __init__(self, tiles_dict):
    self.tiles_dict = tiles_dict

    # initialize unplaced tiles
    self.unplaced_tiles = set()
    for tile_name in self.tiles_dict:
      self.unplaced_tiles.add(tile_name)

    # initialize solved tiles grid
    self.solved = {}

    # queue of spots on solved grid to try next
    self.queue = []
    self.queue.append([0,0])

    # set of spaces explored; only explore each once
    self.visited = set()

  def debug(self):
    print("remaining tiles:")
    print(self.unplaced_tiles)
    print("solve queue:")
    print(self.queue)
    #print("place a tile in 0, -1")
    #self.solved[0] = {}
    #self.solved[0][-1] = "2311"
    #self.unplaced_tiles.remove("2311")
    #print("tile that fits in 0,0")
    #print(self.find_tile_that_fits_in(-1,-1))

  def solve(self):
    while len(self.queue) > 0:
      to_visit = self.queue.pop()

      # checking a coordinate that got added while we were solving
      if tuple(to_visit) in self.visited:
        continue

      found_tile = self.find_tile_that_fits_in(to_visit[0], to_visit[1])
      if found_tile:
        print("Found fit " + found_tile + " at ["+str(to_visit[0])+", "+str(to_visit[1])+"]")
        if to_visit[0] not in self.solved:
          self.solved[to_visit[0]] = {}
        self.solved[to_visit[0]][to_visit[1]] = found_tile

        # add top, right, bottom, left into the queue
        x = -1
        y = 0
        next_coord = [to_visit[0] + x, to_visit[1] + y]
        if tuple(next_coord) not in self.visited:
          self.queue.append(next_coord)

        x = 0
        y = -1
        next_coord = [to_visit[0] + x, to_visit[1] + y]
        if tuple(next_coord) not in self.visited:
          self.queue.append(next_coord)

        x = 1
        y = 0
        next_coord = [to_visit[0] + x, to_visit[1] + y]
        if tuple(next_coord) not in self.visited:
          self.queue.append(next_coord)

        x = 0
        y = 1
        next_coord = [to_visit[0] + x, to_visit[1] + y]
        if tuple(next_coord) not in self.visited:
          self.queue.append(next_coord)

      self.visited.add(tuple(to_visit))


  def find_tile_that_fits_in(self, x, y):
    for tile_name in self.unplaced_tiles:

      # rotate 90s
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()

      # flip_x and rotate
      self.tiles_dict[tile_name].transform_flip_x()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      self.tiles_dict[tile_name].transform_flip_x()

      # flip_y and rotate
      self.tiles_dict[tile_name].transform_flip_y()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      if self.does_tile_fit_in(tile_name, x, y):
        return tile_name
      self.tiles_dict[tile_name].transform_rotate_90()
      self.tiles_dict[tile_name].transform_flip_y()
    return None

  def does_tile_fit_in(self, tile_name, x, y):
    neighbor_up = self.get_tile_at(x, y-1)
    neighbor_right = self.get_tile_at(x+1, y)
    neighbor_down = self.get_tile_at(x, y+1)
    neighbor_left = self.get_tile_at(x-1, y)
    if neighbor_up and not self.tile_fits_with_neighbor(tile_name, neighbor_up, "up"):
      return False
    if neighbor_right and not self.tile_fits_with_neighbor(tile_name, neighbor_right, "right"):
      return False
    if neighbor_down and not self.tile_fits_with_neighbor(tile_name, neighbor_down, "down"):
      return False
    if neighbor_left and not self.tile_fits_with_neighbor(tile_name, neighbor_left, "left"):
      return False
    return True

  def tile_fits_with_neighbor(self, tile_in_question_name, reference_tile_name, direction):
    arr_a = []
    arr_b = []

    tile_in_question = self.tiles_dict[tile_in_question_name].grid
    reference_tile = self.tiles_dict[reference_tile_name].grid

    if direction == "up":

      # arr_a = bottom row of reference_tile
      max_y = max(reference_tile[0].keys())
      min_x = min(reference_tile.keys())
      max_x = max(reference_tile.keys())
      for x in range(min_x, max_x+1):
        arr_a.append(reference_tile[x][max_y])

      # arr_b = top row of tile_in_question
      min_x = min(tile_in_question.keys())
      max_x = max(tile_in_question.keys())
      for x in range(min_x, max_x+1):
        arr_b.append(tile_in_question[x][0])

    elif direction == "right":
      # arr_a = left col of reference_tile
      min_y = min(reference_tile[0].keys())
      max_y = max(reference_tile[0].keys())
      min_x = min(reference_tile.keys())
      max_x = max(reference_tile.keys())
      for y in range(min_y, max_y+1):
        arr_a.append(reference_tile[0][y])

      # arr_b = right col of tile_in_question
      min_y = min(tile_in_question[0].keys())
      max_y = max(tile_in_question[0].keys())
      min_x = min(tile_in_question.keys())
      max_x = max(tile_in_question.keys())
      for y in range(min_y, max_y+1):
        arr_b.append(tile_in_question[max_x][y])

    elif direction == "down":

      # arr_a = top row of reference_tile
      min_x = min(reference_tile.keys())
      max_x = max(reference_tile.keys())
      for x in range(min_x, max_x+1):
        arr_a.append(reference_tile[x][0])

      # arr_b = bottom row of tile_in_question
      max_y = max(tile_in_question[0].keys())
      min_x = min(tile_in_question.keys())
      max_x = max(tile_in_question.keys())
      for x in range(min_x, max_x+1):
        arr_b.append(tile_in_question[x][max_y])

    elif direction == "left":
      # arr_a = right col of reference_tile
      min_y = min(reference_tile[0].keys())
      max_y = max(reference_tile[0].keys())
      min_x = min(reference_tile.keys())
      max_x = max(reference_tile.keys())
      for y in range(min_y, max_y+1):
        arr_a.append(reference_tile[max_x][y])

      # arr_b = left col of tile_in_question
      min_y = min(tile_in_question[0].keys())
      max_y = max(tile_in_question[0].keys())
      min_x = min(tile_in_question.keys())
      max_x = max(tile_in_question.keys())
      for y in range(min_y, max_y+1):
        arr_b.append(tile_in_question[0][y])

    for i in range(len(arr_a)):
      if arr_a[i] != arr_b[i]:
        return False

    return True

  def get_tile_at(self, x, y):
    if x not in self.solved:
      return None
    if y not in self.solved[x]:
      return None
    return self.solved[x][y]

board = Board(tiles_dict)
#board.debug()
board.solve()

#helpers.print_grid(board.solved)

min_x = min(board.solved.keys())
max_x = max(board.solved.keys())
min_y = min(board.solved[0].keys())
max_y = max(board.solved[0].keys())

tl = board.solved[min_x][min_y]
tr = board.solved[max_x][min_y]
bl = board.solved[min_x][max_y]
br = board.solved[max_x][max_y]

print("Part 1 answer:")
print(int(tl)*int(tr)*int(bl)*int(br))

# Part 2 #################################

solved_grid = {}
#helpers.add_to_grid(0, 0, "test", solved_grid)
#helpers.print_grid(solved_grid)

min_x = min(board.solved.keys())
max_x = max(board.solved.keys())
min_y = min(board.solved[0].keys())
max_y = max(board.solved[0].keys())
for x in range(min_x, max_x+1):
  for y in range(min_y, max_y+1):
    tile_name = board.solved[x][y]
    tile_grid = board.tiles_dict[tile_name].grid
    min_i = min(tile_grid.keys())
    max_i = max(tile_grid.keys())
    min_j = min(tile_grid[0].keys())
    max_j = max(tile_grid[0].keys())

    offset_x = x * (max_i+1-2)
    offset_y = y * (max_j+1-2)
    for i in range(min_i, max_i+1):
      if i == 0:
        continue
      elif i == max_i:
        continue
      for j in range(min_j, max_j+1):
        if j == 0:
          continue
        elif j == max_j:
          continue
        helpers.add_to_grid(offset_x + i - 1, offset_y + j - 1, tile_grid[i][j], solved_grid)

print("Search for sea monster in:")
helpers.print_grid(solved_grid)

sea_monster = """..................#.
#....##....##....###
.#..#..#..#..#..#...
"""
sea_monster_grid = helpers.get_grid_from_lines(sea_monster.split("\n"))
print("Sea monster:")
helpers.print_grid(sea_monster_grid)

def is_sea_monster_at(x, y, grid, sea_monster_grid, debug = False):
  if debug:
    print("in is_sea_monster_at")
  min_i = min(sea_monster_grid.keys())
  max_i = max(sea_monster_grid.keys())
  min_j = min(sea_monster_grid[0].keys())
  max_j = max(sea_monster_grid[0].keys())
  for i in range(min_i, max_i+1):
    for j in range(min_j, max_j+1):
      if (x+i) not in grid:
        if debug:
          print("x+i not in grid")
        return False
      if (y+j) not in grid[x+i]:
        if debug:
          print("y+j not in grid")
        return False
      if sea_monster_grid[i][j] == ".":
        continue
      if grid[x+i][y+j] != sea_monster_grid[i][j]:
        if debug:
          print("x="+str(x))
          print("y="+str(y))
          print("i="+str(i))
          print("j="+str(j))
          print("x+i="+str(x+i))
          print("y+j="+str(y+j))
          print("grid and monster pattern mismatch")
          print(grid[x+i][y+j])
          print(sea_monster_grid[i][j])
          print("grid:")
          helpers.print_grid(grid)
          min_x = min(grid.keys())
          max_x = max(grid.keys())
          min_y = min(grid[0].keys())
          max_y = max(grid[0].keys())
          print(min_x)
          print(max_x)
          print(min_y)
          print(max_y)
        return False
      #else:
      #  if debug:
      #    grid[x+i][y+j] = "X"
  return True

def draw_sea_monster_at(x, y, grid, sea_monster_grid, debug=False):
  min_i = min(sea_monster_grid.keys())
  max_i = max(sea_monster_grid.keys())
  min_j = min(sea_monster_grid[0].keys())
  max_j = max(sea_monster_grid[0].keys())
  if debug:
    print("in draw sea monster at")
    print("x = "+str(x))
    print("y = "+str(y))
    print("min_i = "+str(min_i))
    print("max_i = "+str(max_i))
    print("min_j = "+str(min_j))
    print("max_j = "+str(max_j))
  for i in range(min_i, max_i+1):
    for j in range(min_j, max_j+1):
      if (x+i) not in grid:
        if debug:
          print("x not in grid")
        return False
      if (y+j) not in grid[x+i]:
        if debug:
          print("y not in grid")
        return False
      if sea_monster_grid[i][j] == ".":
        continue
      else:
        if debug:
          print("should draw an O")
        grid[x+i][y+j] = "O"
  return True

def scan_sea_monsters(grid, sea_monster_grid, debug=False):
  if debug:
    print("In scan_sea_monsters")
  min_x = min(grid.keys())
  max_x = max(grid.keys())
  min_y = min(grid[0].keys())
  max_y = max(grid[0].keys())
  if debug:
    print(min_x)
    print(max_x)
    print(min_y)
    print(max_y)
  sea_monster_found = False
  for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
      if debug and x == min_x + 2 and y == min_y + 2:
        print("found sea monster at "+str(x)+", "+str(y)+"?")
        print(is_sea_monster_at(x, y, grid, sea_monster_grid, debug))
        draw_sea_monster_at(x, y, grid, sea_monster_grid, debug)
        

      if is_sea_monster_at(x, y, grid, sea_monster_grid):
        sea_monster_found = True
        draw_sea_monster_at(x, y, grid, sea_monster_grid)

  return sea_monster_found

def find_all_sea_monsters(grid, sea_monster_grid):

  # rotate 90s
  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  # flip_x and rotate
  grid = helpers.transform_flip_x(grid)
  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)
  grid = helpers.transform_flip_x(grid)

  # flip_y and rotate
  grid = helpers.transform_flip_y(grid)
  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

  if scan_sea_monsters(grid, sea_monster_grid):
    helpers.print_grid(grid)
    debug_sean(grid, sea_monster_grid)
    return True
  grid = helpers.transform_rotate_90(grid)

def debug_sean(grid, sea_monster_grid):
  #helpers.print_grid(grid)
  #print(is_sea_monster_at(2, 2, grid, sea_monster_grid, True))
  #scan_sea_monsters(grid, sea_monster_grid, True)

  count = 0
  min_x = min(grid.keys())
  max_x = max(grid.keys())
  min_y = min(grid[0].keys())
  max_y = max(grid[0].keys())
  for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
      if grid[x][y] == "#":
        count += 1

  print(count)
  pass

find_all_sea_monsters(solved_grid, sea_monster_grid)





"""
.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#

.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#
"""


