import re

re_card = re.compile("Card\s+(\d+)")
re_winning = re.compile("Card\s+\d+\: ([\d\s]*)\|")
re_mine = re.compile("\| ([\d\s]*)")

with open("Day4/scratchcards.txt", "r") as f:
    cards = f.read().strip().split("\n")
    cards = {
        int(re_card.findall(card)[0]): {
            "winning": re_winning.findall(card)[0]
            .strip()
            .replace("  ", " ")
            .split(" "),
            "mine": re_mine.findall(card)[0].strip().replace("  ", " ").split(" "),
            "multiplier": 1,
        }
        for card in cards
    }

pts = 0
for card_number, card in cards.items():
    match = 0
    for num in card["mine"]:
        if num in card["winning"]:
            match += 1

    copied_cards = [card_number + i for i in range(1, match + 1)]
    for copied_card in copied_cards:
        cards[copied_card]["multiplier"] += 1 * card["multiplier"]
    pts += card["multiplier"]


print(pts)
