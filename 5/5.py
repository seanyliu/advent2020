import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import helpers

def get_seat_number(seat):
  seek_min_row = 0
  seek_max_row = 127
  seek_min_col = 0
  seek_max_col = 7
  for char in seat:
    if char == "F":
      seek_max_row = math.floor((seek_min_row + seek_max_row)/2)
    elif char == "B":
      seek_min_row = math.ceil((seek_min_row + seek_max_row)/2)
    if char == "L":
      seek_max_col = math.floor((seek_min_col + seek_max_col)/2)
    elif char == "R":
      seek_min_col = math.ceil((seek_min_col + seek_max_col)/2)
  return seek_min_row * 8 + seek_min_col


input_lines = helpers.read_lines_from_file('input.txt')

seat_ids = []
for seat in input_lines:
  seat_ids.append(get_seat_number(seat))

print(max(seat_ids))
print(seat_ids.sort())

seat_ids.sort()
print(seat_ids)

for seat in range(min(seat_ids), max(seat_ids)):
  if seat not in seat_ids:
    print("missing seat:"+str(seat))