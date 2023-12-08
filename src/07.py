from utils.api import get_input
from collections import Counter

input_str = get_input(7)

def value(card):
    return "J23456789TQKA".index(card)

def score(hand):
    counts = {}
    for card in hand:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    return sorted(counts.values(), reverse=True)

def bestScore(hand):
    # Assuming J is a wildcard, find the best score for this hand
    cards="23456789TQKA"
    if 'J' in hand:
        return max([bestScore(hand.replace('J', c, 1)) for c in cards])
    return score(hand)

# get best score and append tiebreaker values
def tiebreak(hand):
    sc = bestScore(hand)
    sc.extend([value(x) for x in hand])
    return sc

scores = []
for line in input_str.splitlines():
    hand, bid = line.split()
    scores.append((tiebreak(hand), hand, int(bid)))
scores.sort()


total = 0
for j, s in enumerate(scores):
    total += (j+1) * s[2]
print(total)