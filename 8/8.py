# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers
import console

# functions ##############################

def get_operation(instruction):
  return instruction.split(" ")[0]

def get_argument(instruction):
  return int(instruction.split(" ")[1])

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
c = console.Console(input_lines)
print(c.run())
print(c.get_is_infinite_loop())

# Part 2 #################################
for attempt in range(len(input_lines)):
  new_input_lines = input_lines.copy()
  instruction = new_input_lines[attempt]
  operation = get_operation(instruction)
  argument = get_argument(instruction)
  if operation == "jmp":
    new_input_lines[attempt] = "nop "+str(argument)
  elif operation == "nop":
    new_input_lines[attempt] = "jmp "+str(argument)
  else:
    continue
  c = console.Console(new_input_lines)
  accumulator = c.run()
  if not c.get_is_infinite_loop():
    print(accumulator)

  

