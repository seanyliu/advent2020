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

# returns winner of recursive combat
def recursive_combat(deck1, deck2, debug=False):
  seen_decks = set()
  curr_round = 1

  while len(deck1) > 0 and len(deck2) > 0:

    if debug:
      print("Round "+str(curr_round))
      print("Player 1's deck: "+str(deck1))
      print("Player 2's deck: "+str(deck2))
      curr_round = curr_round + 1

    # prevent infinite loops
    if snapshot(deck1, deck2) in seen_decks:
      if debug:
        print("snapshot seen")
        print(snapshot(deck1, deck2))
        print(seen_decks)
      return 1
    else:
      seen_decks.add(snapshot(deck1, deck2))

    # each player draws a card
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)

    if debug:
      print("Player 1 plays: "+str(card1))
      print("Player 2 plays: "+str(card2))

    round_winner = -1
    if len(deck1) >= card1 and len(deck2) >= card2:
      # both players have at least as many cards remaining in their deck as value of card
      copy1 = deck1[0:card1].copy()
      copy2 = deck2[0:card2].copy()
      round_winner = recursive_combat(copy1, copy2)

    else:
      # one player doens't have enough cards to recurse
      # winner of round is the player with the higher-value card
      if card1 > card2:
        round_winner = 1
      elif card2 > card1:
        round_winner = 2
      else:
        print("ERROR1")

    if debug:
      print("Player "+str(round_winner)+" wins")

    if round_winner == 1:
      deck1.append(card1)
      deck1.append(card2)
    elif round_winner == 2:
      deck2.append(card2)
      deck2.append(card1)
    else:
      print("ERROR2")

  #print(deck1)
  #print(deck2)
  if len(deck1) > 0:
    return 1
  else:
    return 2

def snapshot(deck1, deck2):
  return str(deck1)+str(deck2)

def score_deck(deck):
  multiplier = len(deck)
  score = 0
  for i in deck:
    score = score + i * multiplier
    multiplier = multiplier - 1
  return score

print("winner "+str(recursive_combat(player1_deck, player2_deck, False)))
print(score_deck(player1_deck))
print(score_deck(player2_deck))

"""
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



print(score_deck(player1_deck))
print(score_deck(player2_deck))
"""

# Part 2 #################################
