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
your_ticket = []
valid_tickets = []
fields = {}

count_total_tickets = 0

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

    fields[constraint_type] = []
    fields[constraint_type].append([int(first_range.split("-")[0]), int(first_range.split("-")[1])])
    fields[constraint_type].append([int(second_range.split("-")[0]), int(second_range.split("-")[1])])

    #print(constraint_type + ":" + first_range + ":" + second_range)
  elif section == 1:
    ticket_values = line.split(",")
    for value in ticket_values:
      your_ticket.append(int(value))
  elif section == 2:
    count_total_tickets += 1
    ticket = line
    ticket_values = ticket.split(",")
    is_valid = True
    print(ticket_values)
    for value in ticket_values:
      #print("testing value:"+str(value))
      is_value_in_some_range = False
      for r in ranges:
        start = r[0]
        stop = r[1]
        if int(value) >= start and int(value) <= stop:
          is_value_in_some_range = True
          break
      if is_value_in_some_range:
        is_valid = True
      else:
        is_valid = False
        print("invalid with field: "+value)
        invalids.append(int(value))
        break
    if is_valid:
      valid_ticket = []
      for value in ticket_values:
        valid_ticket.append(int(value))
      valid_tickets.append(valid_ticket)

print("invalid fields:")
print(invalids)
print(sum(invalids))
#print("valid_tickets:")
#print(valid_tickets)

print(str(len(invalids)) + " invalid tickets")
print(str(len(valid_tickets)) + " valid tickets")
print(str(count_total_tickets) + " total tickets")

# Part 2 #################################

def in_range(number, range1, range2):
  return (number >= range1[0] and number <= range1[1]) or (number >= range2[0] and number <= range2[1])

print("your ticket:")
print(your_ticket)

print("valid tickets:")
print(valid_tickets)

print("fields:")
print(fields)

mapped = {}
for field in fields:
  mapped[field] = set()
  for i in range(len(valid_tickets[0])):
    mapped[field].add(i)

for ticket in valid_tickets:
  for i in range(len(ticket)):
    # check if the value isn't possible for the ticket. if so, remove it from the mapped fields possibility
    for field in fields:
      range1 = fields[field][0]
      range2 = fields[field][1]
      value = ticket[i]
      if not in_range(ticket[i], range1, range2):
        mapped[field].remove(i)

for counter in range(len(mapped)):
  # simplify the mapped fields
  for field in mapped:
    if len(mapped[field]) == 1:
      single_key = list(mapped[field])[0]
      print(field+" has a single key: "+str(single_key))
      # remove this key from all other sets
      for key in mapped:
        if key != field and single_key in mapped[key]:
          mapped[key].remove(single_key)

for key in mapped:
  print(key+": "+str(mapped[key]))

"""
mapped = {}

for field in fields:
  print("Testing "+field)
  range1 = fields[field][0]
  range2 = fields[field][1]
  print(range1)
  print(range2)

  for i in range(len(valid_tickets[0])):
    found_column = True
    for ticket in valid_tickets:
      if in_range(ticket[i], range1, range2):
        continue
      else:
        found_column = False
        break
    if found_column:
      mapped[field] = i
      break

print(mapped)

for key in mapped:
  print(key+": "+str(mapped[key]))
"""


mult = 1
for field in mapped:
  if field.split(" ")[0] == "departure":
    print(field)
    mult = mult * your_ticket[list(mapped[field])[0]]

print(mult)



