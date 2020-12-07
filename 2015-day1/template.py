import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import helpers

input_lines = helpers.read_lines_from_file('input.txt')
line = input_lines[0]
floor = 0
char_count = 0
for char in line:
  char_count += 1
  if char == "(":
    floor += 1
  elif char == ")":
    floor -= 1
  if floor == -1:
    print(char_count)
print(floor)