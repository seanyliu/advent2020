# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################
def is_valid(number, preamble):
  for i in range(len(preamble)):
    for j in range(len(preamble)):
      if i == j:
        continue
      if preamble[i] + preamble[j] == number:
        return True
  return False

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')
input_lines = helpers.convert_array_to_int(input_lines)
preamble_size = 25

# Part 1 #################################

part1 = 0

preamble = []
for i in range(preamble_size):
  preamble.append(input_lines[i])

for i in range(preamble_size, len(input_lines)):
  test = is_valid(input_lines[i], preamble)
  if not test:
    print(str(input_lines[i])+" is valid? "+str(test))
    part1 = input_lines[i]
    break
  preamble.pop(0)
  preamble.append(input_lines[i])

# Part 2 #################################

for i in range(len(input_lines)):
  is_done = False
  summation = []
  for j in range(i, len(input_lines)):
    summation.append(input_lines[j])
    if sum(summation) == part1:
      is_done = True
      break
    if sum(summation) > part1:
      break
  if is_done:
    print("Found!")
    print(min(summation) + max(summation))
    break

