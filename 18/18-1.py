# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers
import re

# functions ##############################
def evaluate(parts):
  solution = 0
  last_operand = "+"
  for i in range(len(parts)):

    char = parts[i]

    if char == "+":
      last_operand = "+"
    elif char == "*":
      last_operand = "*"
    else:
      if last_operand == "+":
        solution = solution + int(char)
      elif last_operand == "*":
        solution = solution * int(char)

  return solution

def get_line_parts(line):
  parts = []

  substring = ""
  for i in range(len(line)):

    # space, append previous parts
    if line[i] == " ":
      parts.append(substring)
      substring = ""
      continue

    substring += line[i]

    # last char, append
    if i == len(line) - 1:
      parts.append(substring)
      substring = ""

  return parts

def simplify(line):
  while True:
    print(line)
    m = re.search('\([^\(^\)]+\)', line)
    if m:
      #print(m.group(0))
      #print(m.start())
      #print(m.end())

      substring = m.group(0)
      substring = substring[1:len(substring)-1]
      parts = get_line_parts(substring)
      summation = evaluate(parts)
      #print(summation)

      new_string = line[0:m.start()] + str(summation) + line[m.end():len(line)]
      #print(new_string)
      line = new_string
    else:
      break


  return line

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
sum_of_answers = 0
for line in input_lines:
  line = simplify(line)
  parts = get_line_parts(line)
  sum_of_answers += evaluate(parts)

print(sum_of_answers)


# Part 2 #################################
