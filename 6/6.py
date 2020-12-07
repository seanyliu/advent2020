import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import helpers

input_lines = helpers.read_lines_from_file('input.txt')

"""
# part 1
group_questions = []
group_answers = set()
for line_index in range(len(input_lines)):
  line = input_lines[line_index]
  print(line)
  if line == "":
    group_questions.append(len(group_answers))
    group_answers = set()
    continue
  for char in line:
    group_answers.add(char)
  if line_index == len(input_lines)-1:
    group_questions.append(len(group_answers))
    group_answers = set()
print(sum(group_questions))
"""

# part 2
group_questions = []
group_answers = set()
last_line_break_index = -1
for line_index in range(len(input_lines)):
  #print(line_index)
  line = input_lines[line_index]

  # group break
  if line == "":
    group_questions.append(len(group_answers))
    group_answers = set()
    last_line_break_index = line_index
    #print("end group line")
    #print(group_answers)
    continue

  # new group
  if (line_index == last_line_break_index+1):
    #print("first in group:"+line)
    for char in line:
      group_answers.add(char)
    #print(group_answers)
  else:
    new_answers = set()
    for char in line:
      new_answers.add(char)
    group_answers = group_answers.intersection(new_answers)

  # special case last line
  if line_index == len(input_lines)-1:
    group_questions.append(len(group_answers))
    group_answers = set()
print(group_questions)
print(sum(group_questions))
