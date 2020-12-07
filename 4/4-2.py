import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import re
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
      print("missing key "+required)
      return False
    key = required
    value = passport[required]
    if key == "byr":
      if len(value) != 4:
        print("invalid byr")
        return False
      if not (int(value) >= 1920 and int(value) <= 2002):
        print("invalid byr")
        return False
    elif key == "iyr":
      if len(value) != 4:
        print("invalid iyr")
        return False
      if not (int(value) >= 2010 and int(value) <= 2020):
        print("invalid iyr")
        return False
    elif key == "eyr":
      if len(value) != 4:
        print("invalid eyr")
        return False
      if not (int(value) >= 2020 and int(value) <= 2030):
        print("invalid eyr")
        return False
    elif key == "hgt":
      is_cm = "cm" in value
      is_in = "in" in value
      if not is_cm and not is_in:
        print("invalid hgt")
        return False
      height = value[:-2]
      if is_cm:
        if not (int(height) >= 150 and int(height) <= 193):
          print("invalid hgt")
          return False
      elif is_in:
        if not (int(height) >= 59 and int(height) <= 76):
          print("invalid hgt")
          return False
    elif key == "hcl":
      if "#" not in value:
        print("invalid hcl")
        return False
      color = value[1:]
      if len(color) != 6:
        print("invalid hcl")
        return False
      valid = re.compile(r"[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]")
      if not valid.match(color):
        print("invalid hcl "+value)
        return False
    elif key == "ecl":
      if value not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        print("invlaid ecl")
        return False
    elif key == "pid":
      valid = re.compile(r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")
      if not (valid.match(value) and len(value) == 9):
        print("invlaid pid")
        return False
    else:
      return True
  return True

input_lines = helpers.read_lines_from_file('input.txt')
passports = get_passports_from_lines(input_lines)

valid_count = 0
for passport in passports:
  if is_valid_passport(passport):
    valid_count += 1
print(valid_count)
