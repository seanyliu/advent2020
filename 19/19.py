# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers
import regex

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################

# Extract rules and messages

rules_lines = []
messages = []

finished_rules = False
for line in input_lines:
  if not finished_rules:
    if line != "":
      rules_lines.append(line)
    else:
      finished_rules = True
      continue
  else:
    messages.append(line)

#print(rules_lines)
#print(messages)

# Convert rules into a dictionary

rules = {}

for line in rules_lines:
  rule_id = line.split(": ")[0]
  rule_desc = line.split(": ")[1]
  rules[rule_id] = rule_desc

print(rules)

def get_exp_from_rule(rule_id, rules):
  desc = rules.get(rule_id, False)
  parts = desc.split(" | ")
  if len(parts) == 1:
    if rule_id == "8":
      return "("+get_exp_from_rule_no_paren(parts[0], rules)+")+"
    else:
      return get_exp_from_rule_no_paren(parts[0], rules)
  else:
    return "((" + get_exp_from_rule_no_paren(parts[0], rules) + ")|(" + get_exp_from_rule_no_paren(parts[1], rules) + "))"

def get_exp_from_rule_no_paren(desc, rules):
  exp = ""
  for var in desc.split(" "):
    if var == '"a"':
      exp += "a"
    elif var == '"b"':
      exp += "b"
    elif var == "|":
      pass
    else:
      exp += get_exp_from_rule(var, rules)
    #print(var)
  return exp

print(get_exp_from_rule('0', rules))

print("begin counting matches")
count_matches = 0
exp = "^"+get_exp_from_rule('0', rules)+"$"

exp_list = []
for i in range(10):
  expression = "42 31"
  for j in range(1,i):
    expression = "42 " + expression + " 31"
  #print(expression)
  exp_list.append("^" + get_exp_from_rule_no_paren("8 "+expression, rules) + "$")
#print(exp_list)


for message in messages:

  original_message = message

  # part 2
  for exp in exp_list:
    compiled = regex.compile(exp)
    if compiled.match(message):
      count_matches += 1
      print(original_message)
      break


  

print(count_matches)

#print(exp42)


"""

    elif rule_id == "11":
      return "(?P<rule11>"+get_exp_from_rule_no_paren("42", rules)+"(?P=rule11)?"+get_exp_from_rule_no_paren("31", rules)+")"
    else:
"""
"""
#strip rule 11
#exp42 = "(("+get_exp_from_rule_no_paren('9 14', rules)+")|("+get_exp_from_rule_no_paren('10 1', rules)+"))"
#exp42 = get_exp_from_rule_no_paren('42 42 42 42 42 31 31 31 31', rules)

#exp42 = "^"+get_exp_from_rule_no_paren('8 42 42 31 31', rules)+"$"
print("DEBUG =======")
test = "babbbbaabbbbbabbbbbbaabaaabaaa"
print(test)

print("REPLAC =======")


exp42 = get_exp_from_rule_no_paren('42 31', rules)
compiled42 = regex.compile(exp42)
match = compiled42.search(test)
replacement = match.group(0)

exp42 = get_exp_from_rule_no_paren('42 42 31 31', rules)
compiled42 = regex.compile(exp42)
while True:
  match = compiled42.search(test)
  if match:
    #print("destroy this:"+match.group(0))
    #print("original:"+message)
    test = regex.sub(exp42, replacement, test)
    #print("new     :"+message)
  else:
    break
print(test)

print("TEST ======")

exp42 = get_exp_from_rule_no_paren('8 42 42 31', rules)
compiled42 = regex.compile(exp42)
match = compiled42.search(test)
print(match)
print(match.group(0))

"""




"""
exp42 = get_exp_from_rule_no_paren('31', rules)
#print(exp42)
compiled42 = regex.compile(exp42)
test = "bbabaaabbababababaaa"
print(test)
match = compiled42.match(test)
print(match)
print(match.group(0))
"""

"""
bbabbbbaabaabba
ababaaaaaabaaab
ababaaaaabbbaba
aaaaabbaabaaaaababaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
"""
