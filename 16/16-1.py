# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
section = 0
# 0 = constraints
# 1 = your ticket
# 2 = nearby tickets

ranges = []
invalids = []

for line in input_lines:

  # process section
  if line == "your ticket:":
    section = 1
    continue
  elif line == "nearby tickets:":
    section = 2
    continue
  elif line == "":
    continue

  if section == 0:
    constraint_type = line.split(": ")[0]
    first_range = line.split(": ")[1].split(" or ")[0]
    second_range = line.split(": ")[1].split(" or ")[1]
    ranges.append([int(first_range.split("-")[0]), int(first_range.split("-")[1])])
    ranges.append([int(second_range.split("-")[0]), int(second_range.split("-")[1])])
    #print(constraint_type + ":" + first_range + ":" + second_range)
  elif section == 1:
    pass
  elif section == 2:
    tickets = line.split(",")
    for ticket in tickets:
      is_valid = False
      for r in ranges:
        start = r[0]
        stop = r[1]
        if int(ticket) >= start and int(ticket) <= stop:
          is_valid = True
          break
      if not is_valid:
        invalids.append(int(ticket))


print(invalids)
print(sum(invalids))


# Part 2 #################################
