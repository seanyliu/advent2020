import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import helpers

input_lines = helpers.read_lines_from_file('input.txt')

def find2020():
  for item1 in input_lines:
    for item2 in input_lines:
      for item3 in input_lines:
        int1 = int(item1)
        int2 = int(item2)
        int3 = int(item3)
        if (int1 + int2 + int3 == 2020):
          print(int1 * int2 * int3)
          return True

find2020()


