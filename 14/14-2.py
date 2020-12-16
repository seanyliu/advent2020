# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################
def extend_digit(digit):
  extended_digit = digit
  for i in range(len(digit),36):
    extended_digit = "0" + extended_digit
  return extended_digit

def apply_mask(digit, mask):
  masked_digit = list(digit)
  for i in range(len(mask)):
    if mask[i] != "X":
      masked_digit[i] = mask[i]
  return "".join(masked_digit)

def apply_memory_mask(digit, mask):
  addresses = []
  addresses.append("")
  for i in range(len(mask)):
    if mask[i] == "0":
      for a in range(len(addresses)):
        addresses[a] = addresses[a] + digit[i]
      pass
    elif mask[i] == "1":
      for a in range(len(addresses)):
        addresses[a] = addresses[a] + "1"
      pass
    elif mask[i] == "X":
      for a in range(len(addresses)):
        addresses.append(addresses[a] + "1")
        addresses[a] = addresses[a] + "0"
      pass
  return addresses

def get_digit(str):
  return int(str,2)

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
mask = input_lines[0].split(" = ")[1]
memory = {}

for line in input_lines:
  if (line.split(" = ")[0] == "mask"):
    mask = line.split(" = ")[1]
  else:
    mem_address = line.split(" = ")[0].split("[")[1].split("]")[0]
    mem_address = extend_digit(str(bin(int(mem_address)))[2:])
    decimal_value = line.split(" = ")[1]
    print("writing to:"+mem_address)
    print("decimal_value:"+decimal_value)

    addresses = apply_memory_mask(mem_address, mask)
    for a in addresses:
      memory[get_digit(a)] = decimal_value

    """
    mem_value = str(bin(int(decimal_value)))[2:]
    mem_value = extend_digit(mem_value)
    #print("original:"+mem_value + " ("+str(get_digit(mem_value))+")")
    #print("mask    :"+mask)
    mem_value = apply_mask(mem_value, mask)
    #print("masked  :"+mem_value + " ("+str(get_digit(mem_value))+")")
    memory[mem_address] = mem_value
    """

summation = 0
for address in memory:
  #print(memory[address])
  #print(get_digit(memory[address]))
  #summation += get_digit(memory[address])
  summation += int(memory[address])

print(summation)

# Part 2 #################################
