import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import helpers

input_lines = helpers.read_lines_from_file('input.txt')

valid = 0

for line in input_lines:
  line_parts = line.split()
  index_1 = int(line_parts[0].split("-")[0])
  index_2 = int(line_parts[0].split("-")[1])
  letter = line_parts[1].split(":")[0]
  password = line_parts[2]
  matches = 0
  if password[index_1-1] == letter:
    matches = matches + 1
    if password[index_2-1] == letter:
      matches = matches + 1
      if matches == 1:
        valid = valid + 1

        print(valid)

""" part 1:
for line in input_lines:
    line_parts = line.split()
    min_occurrences = int(line_parts[0].split("-")[0])
    max_occurrences = int(line_parts[0].split("-")[1])
    letter = line_parts[1].split(":")[0]
    password = line_parts[2]
    count = password.count(letter)
    if count >= min_occurrences and count <= max_occurrences:
        valid = valid+1
        """