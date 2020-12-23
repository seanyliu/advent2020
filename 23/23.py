# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

class Cup:
  def __init__(self, label, next):
    self.label = label
    self.next = next

def print_cups(first_cup):
  s = "("+str(first_cup.label)+") "
  cup = first_cup
  while True:
    next_cup = cup.next
    if next_cup.label != first_cup.label:
      s += str(next_cup.label) + " "
      cup = next_cup
    else:
      break
  return s

def print_pickup(first_cup):
  s = str(first_cup.label) + " "
  cup = first_cup
  for i in range(2):
    next_cup = cup.next
    s += str(next_cup.label) + " "
    cup = next_cup
  return s

def pickup_set(first_cup):
  s = set()
  s.add(first_cup.label)
  cup = first_cup
  for i in range(2):
    next_cup = cup.next
    s.add(next_cup.label)
    cup = next_cup
  return s

def part1(first_cup):
  s = ""
  cup = first_cup
  while True:
    next_cup = cup.next
    if next_cup.label != first_cup.label:
      s += str(next_cup.label)
      cup = next_cup
    else:
      break
  return s

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 2 #################################

# global variables
cup_pointers = {}
first_cup = None
min_label = None
max_label = None

# special case first cup
first_cup = Cup(int(input_lines[0][0]), None)
cup_pointers[first_cup.label] = first_cup
min_label = first_cup.label
max_label = first_cup.label

# create cups and link them together
previous_cup = first_cup
for char in input_lines[0][1:]:

  # create a new cup
  cup = Cup(int(char), None)

  # update global variables
  cup_pointers[cup.label] = cup
  if cup.label > max_label:
    max_label = cup.label
  if cup.label < min_label:
    min_label = cup.label

  # link up the cups
  previous_cup.next = cup
  previous_cup = cup

# extend the cup labels to 1M
new_label = max_label+1
for i in range(1000000-len(input_lines[0])):

  # create a new cup
  cup = Cup(new_label, None)

  # update global variables
  cup_pointers[cup.label] = cup
  if cup.label > max_label:
    max_label = cup.label
  if cup.label < min_label:
    min_label = cup.label

  # link up the cups
  previous_cup.next = cup
  previous_cup = cup
  new_label += 1

# tie together the last cup and the first
previous_cup.next = first_cup

# run moves 10M times
current_cup = first_cup
for i in range(10000000):

  # pick up cups
  pickedup_set = pickup_set(current_cup.next)
  pickedup_start = current_cup.next
  pickedup_end = pickedup_start.next.next

  # find the destionation cup
  destination_cup_label = current_cup.label - 1
  while destination_cup_label in pickedup_set or destination_cup_label < min_label:
    destination_cup_label = destination_cup_label - 1
    if destination_cup_label < min_label:
      destination_cup_label = max_label

  if False:
    print("-- move "+str(i+1)+" --")
    print("cups: "+print_cups(current_cup))
    print("pick up: "+print_pickup(current_cup.next))
    print("destination: "+str(destination_cup_label))

  # rewire the cups
  current_cup.next = pickedup_end.next # cut out the picked up cups
  pickedup_end.next = cup_pointers[destination_cup_label].next # splice in picked up next to destination
  cup_pointers[destination_cup_label].next = pickedup_start

  # increment current cup for step 2
  current_cup = current_cup.next

if False:
  print("-- final --")
  print("cups: "+print_cups(current_cup))
  print(part1(cup_pointers[1]))

if True:
  # print solution for part 2
  neighbor1 = cup_pointers[1].next
  neighbor2 = neighbor1.next
  print("neighbor1: "+str(neighbor1.label))
  print("neighbor2: "+str(neighbor2.label))
  print(str(neighbor1.label * neighbor2.label))

