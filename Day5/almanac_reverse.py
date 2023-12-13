import re

from rich.pretty import pprint

with open("Day5/almanac.txt", "r") as f:
    almanac = f.read().strip().replace("\n", " ")

re_seeds = re.compile("seeds\:([0-9 ]*)")
seeds = [int(seed) for seed in re_seeds.findall(almanac)[0].strip().split(" ")]
map_dict = {
    "seed": {
        "source": None,
        "ranges": [
            {"destination": (seeds[i], seeds[i] + seeds[i + 1])}
            for i in range(0, len(seeds), 2)
        ],
    }
}


re_map = re.compile("([a-z]*)-to-([a-z]*) map:([0-9 ]*)")
for _map in re_map.findall(almanac):
    source, destination = _map[0:2]
    map_dict[destination] = {"source": source, "ranges": []}

    numbers = list(map(int, _map[2].strip().split(" ")))
    for i in range(0, len(numbers), 3):
        map_dict[destination]["ranges"].append(
            {
                "source": (numbers[i + 1], numbers[i + 1] + numbers[i + 2]),
                "destination": (numbers[i], numbers[i] + numbers[i + 2]),
            }
        )

pprint(map_dict)


def search_source_value(destination, destination_value):
    global map_dict

    ranges = map_dict[destination]["ranges"]

    if destination == "seed":
        for _range in ranges:
            if _range["destination"][0] <= destination_value < _range["destination"][1]:
                print("caralho")
                return True
        return False

    source = map_dict[destination]["source"]

    isinrange = False
    for _range in ranges:
        if _range["destination"][0] <= destination_value < _range["destination"][1]:
            isinrange = True
            offset = destination_value - _range["destination"][0]
            source_value = _range["source"][0] + offset
            found = search_source_value(
                destination=source, destination_value=source_value
            )
            if found:
                return True
    if not isinrange:
        source_value = destination_value
        found = search_source_value(destination=source, destination_value=source_value)
        if found:
            return True
    return False


location = 0
location_found = False

while not location_found:
    location += 1
    location_found = search_source_value("location", location)

print(location)
