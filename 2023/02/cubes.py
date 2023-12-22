import re

with open("Day2/record.txt", "r") as f:
    games = f.readlines()


def parse_round(r: list[str]):
    round_colors = []
    for s in r:
        colors = {}
        for color in ["blue", "red", "green"]:
            num_cubes_color = re.findall("(\d+) " + color, s)
            if num_cubes_color:
                colors[color] = int(num_cubes_color[0])
        round_colors.append(colors)
    return round_colors


parsed_games = {
    re.compile("Game (\d+)").findall(game_num)[0]: parse_round(round)
    for game in games
    for game_num, rounds in (game.split(":"),)
    for round in (rounds.split(";"),)
}

available_cubes = {"red": 12, "green": 13, "blue": 14}


def validate_game(rounds):
    required_cubes = {"red": [0], "blue": [0], "green": [0]}
    valid = True
    for round in rounds:
        for color, num_cubes in round.items():
            required_cubes[color].append(num_cubes)
            # print(color, num_cubes, available_cubes[color])
            if num_cubes > available_cubes[color]:
                valid = False
    power = (
        max(required_cubes["red"])
        * max(required_cubes["blue"])
        * max(required_cubes["green"])
    )
    return valid, power


validated_games = []
powers = []
for game, rounds in parsed_games.items():
    # print("Game", game)
    game_validated, power = validate_game(rounds)
    powers.append(power)
    if game_validated:
        validated_games.append(int(game))
    else:
        continue

print(validated_games)
print(sum(validated_games))
print(powers)
print(sum(powers))
