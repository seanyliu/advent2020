import helpers

input_lines = helpers.read_lines_from_file('input.txt')

sum_left = input_lines
sum_right = input_lines
sum_third = input_lines

for element_left in sum_left:
  is_sum_found = False
  for element_right in sum_right:
    for element_third in sum_third:
      int_left = int(element_left)
      int_right = int(element_right)
      int_third = int(element_third)
      if (int_left + int_right + int_third == 2020):
        is_sum_found = True
        print(int_left * int_right * int_third)
        break
    if (is_sum_found):
      break
  if (is_sum_found):
    break


