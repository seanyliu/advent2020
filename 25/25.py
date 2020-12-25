# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')
card_public_key = int(input_lines[0])
#card_public_key = 5764801
door_public_key = int(input_lines[1])

print("card public key: "+str(card_public_key))
print("door public key: "+str(door_public_key))

# Part 1 #################################

def transform_subject_number_up(subject_number, loop_size):
  start = 1
  for i in range(loop_size):
    start = start * subject_number
    start = start % 20201227
  return start

transform_memory = {}
transform_memory[7] = {}
def transform_subject_number(subject_number, loop_size):
  if subject_number in transform_memory and loop_size in transform_memory[subject_number]:
    return transform_memory[subject_number][loop_size]
  if loop_size == 0:
    return 1

  start = transform_subject_number(subject_number, loop_size-1)
  start = start * subject_number
  start = start % 20201227
  transform_memory[7][loop_size] = start
  return start

# card and door public keys used 7 as the subject number
card_loop_size = 250288
while False:
  if transform_subject_number(7, card_loop_size) == card_public_key:
    break
  else:
    card_loop_size += 1
print("Card loop size: "+str(card_loop_size))

door_loop_size = 14519824
while False:
  if transform_subject_number(7, door_loop_size) == door_public_key:
    break
  else:
    door_loop_size += 1
print("Door loop size: "+str(door_loop_size))

#Card loop size: 250288
#Door loop size: 14519824

print(transform_subject_number_up(door_public_key, card_loop_size))
print(transform_subject_number_up(card_public_key, door_loop_size))


# Part 2 #################################
