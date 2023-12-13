from rich.pretty import pprint
from collections import Counter

CARDS = "".join(list(reversed("AKQT98765432J")))

with open("camel_cards.txt", "r") as f:
    game = f.read().strip().split("\n")

hands = []
for i in game:
    cards, bid = i.split(" ")
    hands.append({"cards": cards, "bid": int(bid)})


def compute_points(cards: str) -> int:
    points = 0
    for n in range(len(cards)):
        points += (CARDS.index(cards[n]) + 1) * 14 ** (len(cards) - n)

    higher_type = 0
    for joker in CARDS:
        temp_cards = cards.replace("J", joker)
        counter_cards = Counter(temp_cards)
        if 5 in counter_cards.values():
            type = 6
        elif 4 in counter_cards.values():
            type = 5
        elif 3 in counter_cards.values() and 2 in counter_cards.values():
            type = 4
        elif 3 in counter_cards.values():
            type = 3
        elif 2 == Counter(counter_cards.values())[2]:
            type = 2
        elif 1 == Counter(counter_cards.values())[2]:
            type = 1
        else:
            type = 0
        if type > higher_type:
            higher_type = type
    type = {
        6: "Five of a kind",
        5: "Four of a kind",
        4: "Full house",
        3: "Three of a kind",
        2: "Two pairs",
        1: "One pair",
        0: "High card",
    }[higher_type]
    points += higher_type * (14 ** (len(cards) + 1))
    return points, type


for hand in hands:
    hand["points"], hand["type"] = compute_points(hand["cards"])


hands = sorted(hands, key=lambda x: x["points"], reverse=True)

for k, hand in enumerate(hands, start=0):
    hand["rank"] = len(hands) - k

pprint(hands)

total_winnings = 0
for hand in hands:
    total_winnings += hand["rank"] * hand["bid"]

print(total_winnings)
