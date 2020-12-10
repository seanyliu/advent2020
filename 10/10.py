# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################


# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')
input_lines = helpers.convert_array_to_int(input_lines)

# Part 1 #################################
input_lines.sort()

current_jolt = 0
count_singles = 0
count_triples = 1 # built-in is 3 higher
for jolt in input_lines:
  delta = jolt - current_jolt
  if delta == 1:
    count_singles += 1
  elif delta == 3:
    count_triples += 1
  current_jolt = jolt
print(count_singles * count_triples)

# Part 2 #################################

#input_lines.append(input_lines[len(input_lines)-1]+3)
input_lines.insert(0, 0)

paths_to_get_to = {}

print(input_lines)

for i in range(len(input_lines)):
  curr_jolt = input_lines[i]
  print("starting at curr_jolt: "+str(curr_jolt))
  for j in range(i+1, len(input_lines)):
    next_jolt = input_lines[j]
    if next_jolt - curr_jolt <= 3:
      if next_jolt not in paths_to_get_to:
        paths_to_get_to[next_jolt] = set()
      paths_to_get_to[next_jolt].add(curr_jolt)
    else:
      break
print(paths_to_get_to)

mem_count = {}
# special count the first node as a 1
mem_count[input_lines[0]] = 1

for node in paths_to_get_to:

  if node not in mem_count:
    mem_count[node] = 0

  count = 0
  for incoming in paths_to_get_to[node]:
    count += mem_count[incoming]
  mem_count[node] = count

print(mem_count)
print(mem_count[input_lines[len(input_lines)-1]])

# basically we want to multiply the number of ways that you can get to each number together
"""

(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

{4: {1}, 5: {4}, 6: {4, 5}, 7: {4, 5, 6}, 10: {7}, 11: {10}, 12: {10, 11}, 15: {12}, 16: {15}, 19: {16}}

1 4 5


"""

