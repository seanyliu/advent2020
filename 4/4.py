import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import helpers

def get_passports_from_lines(input_lines):
  passports = []
  passport_index = 0
  for line in input_lines:
    if line == "":
      passport_index += 1
      continue
    if passport_index >= len(passports):
      passports.append({})

    pairs = line.split()    
    for pair in pairs:
      key_value = pair.split(":")
      key = key_value[0]
      value = key_value[1]
      #print("key="+key+";value="+value)
      passports[passport_index][key] = value
  return passports

def is_valid_passport(passport):
  required_keys = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    #"cid"
  }
  for required in required_keys:
    if required not in passport:
      return False
  return True

input_lines = helpers.read_lines_from_file('input.txt')
passports = get_passports_from_lines(input_lines)

valid_count = 0
for passport in passports:
  if is_valid_passport(passport):
    valid_count += 1
print(valid_count)
