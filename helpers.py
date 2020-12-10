def read_lines_from_file(file_name):
  input_file = open(file_name, "r")
  input_lines = input_file.readlines()
  input_file.close()
  cleaned_lines = []
  for line in input_lines:
    cleaned_lines.append(line.strip())
  return cleaned_lines

def convert_array_to_int(arr):
  int_arr = []
  for i in arr:
    int_arr.append(int(i))
  return int_arr

def get_grid_from_lines(input_lines):
  grid = {}
  y = 0
  for line in input_lines:
    x = 0
    for c in line:
      if x not in grid:
        grid[x] = {}
      grid[x][y] = c
      # print(str(x)+","+str(y)+"="+c)
      x = x+1
    y = y+1
  return grid

def print_grid(grid):
  min_y = min(grid[0].keys())
  max_y = max(grid[0].keys())
  for y in range(min_y, max_y+1):
    line = ""
    min_x = min(grid.keys())
    max_x = max(grid.keys())
    for x in range(min_x, max_x+1):
      #print(str(x) + "," + str(y) + "=" + grid[x][y])
      line = line + grid[x][y]
    print(line)

def get_grid_col_count(grid):
  return len(grid.keys())

def get_grid_row_count(grid):
  return len(grid[0].keys())