# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
earliest_depart = int(input_lines[0])
print("earliest_depart="+str(earliest_depart))

buses = []
for id in input_lines[1].split(","):
  if id != "x":
    buses.append(int(id))
print(buses)

min_depart = math.inf
min_id = 0
for bus in buses:
  bus_departs = bus - earliest_depart % bus
  if bus_departs < min_depart:
    min_depart = bus_departs
    min_id = bus

print("min_depart = "+str(min_depart))
print("part1 = "+str(min_depart * min_id))

# Part 2 #################################

# y = x**(p-2) mod p  # Pseudocode
# y = pow(x, p-2, p)

# use the chinese remainder theorem
# https://brilliant.org/wiki/chinese-remainder-theorem/

#buses = [7, 13, 59]
#a = [0, -1, -4]
buses = []
a = []
y = []
z = []

inc = 0
for id in input_lines[1].split(","):
  if id != "x":
    buses.append(int(id))
    a.append(inc)
  inc -= 1
print(buses)
print(a)

N = 1
for bus in buses:
  N = N * bus

for bus in buses:
  y.append(int(N / bus))

print(y)

for i in range(len(buses)):
  z.append(pow(y[i], -1, buses[i]))
x = 0
for i in range(len(buses)):
  x += a[i] * y[i] * z[i]

print(x % N)

