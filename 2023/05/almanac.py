import re
import sys

re_seeds = re.compile("seeds\:([0-9 ]*)")
re_map = re.compile("([a-z]*)-to-([a-z]*) map:([0-9 ]*)")

with open("almanac_test.txt", "r") as f:
    almanac = f.read()


def main(almanac):
    almanac = almanac.strip().replace("\n", " ")
    seeds = [int(seed) for seed in re_seeds.findall(almanac)[0].strip().split(" ")]
    seeds_range = [
        range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)
    ]

    total_seeds = sum([len(seed_range) for seed_range in seeds_range])

    maps = re_map.findall(almanac)

    map_dict = {}
    for map in maps:
        # map = maps[0]
        source = map[0]
        destination = map[1]
        numbers = [int(number) for number in map[2].strip().split(" ")]
        map_dict[source] = {"destination": destination, "ranges": []}
        for i in range(0, len(numbers), 3):
            map_dict[source]["ranges"].append(
                {
                    "source": range(numbers[i + 1], numbers[i + 1] + numbers[i + 2]),
                    "destination": range(numbers[i], numbers[i] + numbers[i + 2]),
                }
            )
    # range(1, 2).start
    i = 0
    location = None
    for seed_range in seeds_range:
        for seed in seed_range:
            # seed=seeds[3]
            source = "seed"
            source_value = seed

            while source != "location":
                ranges = map_dict[source]["ranges"]
                destination_value = None
                for _range in ranges:
                    # _range=ranges[1]
                    if source_value in _range["source"]:
                        delta = source_value - _range["source"].start
                        destination_value = _range["destination"].start + delta
                        break
                if destination_value is None:
                    destination_value = source_value
                # print(map_dict[source]["destination"], destination_value)
                source = map_dict[source]["destination"]
                source_value = destination_value
            if location is None:
                location = source_value
            elif location < source_value:
                continue
            else:
                location = source_value

    print(location)


main(almanac)
