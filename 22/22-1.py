# regular imports ########################
import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers

# functions ##############################

# actual code ############################
input_lines = helpers.read_lines_from_file('input.txt')

# Part 1 #################################
player1_deck = []
player2_deck = []
array_pointer = None
for line in input_lines:
  if line == "Player 1:":
    array_pointer = player1_deck
  elif line == "Player 2:":
    array_pointer = player2_deck
  elif line == "":
    continue
  else:
    array_pointer.append(int(line))

print("Start of game")
print(player1_deck)
print(player2_deck)

curr_round = 1
while len(player1_deck) > 0 and len(player2_deck) > 0:
  print("Round "+str(curr_round))
  print("Player 1's deck: "+str(player1_deck))
  print("Player 2's deck: "+str(player2_deck))
  player1_card = player1_deck.pop(0)
  player2_card = player2_deck.pop(0)
  print("Player 1 plays: "+str(player1_card))
  print("Player 2 plays: "+str(player2_card))
  if player1_card > player2_card:
    print("Player 1 wins the round!")
    player1_deck.append(player1_card)
    player1_deck.append(player2_card)
  elif player2_card > player1_card:
    print("Player 2 wins the round!")
    player2_deck.append(player2_card)
    player2_deck.append(player1_card)
  else:
    print("Unexpected card tie")
  curr_round += 1

print("End of game")
print(player1_deck)
print(player2_deck)

def score_deck(deck):
  multiplier = len(deck)
  score = 0
  for i in deck:
    score = score + i * multiplier
    multiplier = multiplier - 1
  return score

print(score_deck(player1_deck))
print(score_deck(player2_deck))


# Part 2 #################################
