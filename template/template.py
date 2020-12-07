# regular imports
import math

# import helpers
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import helpers

# functions
def count_trees(x_inc, y_inc):
  x = 0
  y = 0
  trees = 0
  while y < helpers.get_grid_row_count(grid):
    x = x + x_inc
    y = y + y_inc
    c = grid[x % helpers.get_grid_col_count(grid)][y % helpers.get_grid_row_count(grid)]
    if c == "#":
      trees = trees + 1
  return trees

# actual code
input_lines = helpers.read_lines_from_file('input_test.txt')

grid = helpers.get_grid_from_lines(input_lines)
print(count_trees(1,1) * count_trees(3,1) * count_trees(5,1) * count_trees(7,1) * count_trees(1,2))