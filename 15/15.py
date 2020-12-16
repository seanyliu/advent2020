# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
inputs = input_lines[0].split(",")
for i in range(len(inputs)):
  inputs[i] = int(inputs[i])

last_spoken = {} # dictionary of when a number was last spoken

previous = -1
for i in range(2020):
  #print("turn "+str(i)+"; previous="+str(previous))
  if i < len(inputs):
    previous = inputs[i]
    last_spoken[previous] = []
    last_spoken[previous].append(i+1)
  elif previous in last_spoken and len(last_spoken[previous]) < 2:
    previous = 0
    if previous not in last_spoken:
      last_spoken[previous] = []
    last_spoken[previous].append(i+1) # i+1 since turns are 1-indexed
  else:
    previous = last_spoken[previous][len(last_spoken[previous])-1] - last_spoken[previous][len(last_spoken[previous])-2]
    if previous not in last_spoken:
      last_spoken[previous] = []
    last_spoken[previous].append(i+1) # i+1 since turns are 1-indexed

# print(last_spoken)
print(previous)

# Part 2 #################################
