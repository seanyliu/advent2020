# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers
import re

# functions ##############################
def parentheses(line):
  while True:
    #print(line)
    m = re.search('\([^\(^\)]+\)', line)
    if m:
      #print(m.group(0))
      #print(m.start())
      #print(m.end())

      substring = m.group(0)
      substring = substring[1:len(substring)-1]
      summation = evaluate(substring)
      #print(summation)

      new_string = line[0:m.start()] + str(summation) + line[m.end():len(line)]
      #print(new_string)
      line = new_string
    else:
      break
  return line

def evaluate(line):

  # process all addition
  while True:
    #print(line)
    m = re.search('[0-9]+\s\+\s[0-9]+', line)
    if m:
      substring = m.group(0)
      left = int(substring.split(" + ")[0])
      right = int(substring.split(" + ")[1])
      summation = left + right
      new_string = line[0:m.start()] + str(summation) + line[m.end():len(line)]
      line = new_string
    else:
      break

  # process all multiplication
  # process all addition
  while True:
    #print(line)
    m = re.search('[0-9]+\s\*\s[0-9]+', line)
    if m:
      substring = m.group(0)
      left = int(substring.split(" * ")[0])
      right = int(substring.split(" * ")[1])
      summation = left * right
      new_string = line[0:m.start()] + str(summation) + line[m.end():len(line)]
      line = new_string
    else:
      break

  return int(line)

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
sum_of_answers = 0
for line in input_lines:
  line = parentheses(line)
  sum_of_answers += evaluate(line)

  #parts = get_line_parts(line)
  #sum_of_answers += evaluate_parts(parts)

print(sum_of_answers)


# Part 2 #################################
