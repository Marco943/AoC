from argparse import ArgumentParser
from importlib import import_module

arg_parser = ArgumentParser()
arg_parser.add_argument("-y", "--year", required=True)
arg_parser.add_argument("-d", "--day", required=True)

args = arg_parser.parse_args()

YEAR: int = args.year
DAY: int = args.day

module = import_module(f"{YEAR}.{DAY:0>2}.{YEAR[-2:]}{DAY:0>2}")

print("=" * 20 + " PART 1 " + "=" * 20)
print("Test:", module.part_1(f"{YEAR}/{DAY:0>2}/test.txt"))
print("Input:", module.part_1(f"{YEAR}/{DAY:0>2}/input.txt"))
print("=" * 20 + " PART 2 " + "=" * 20)
print("Test:", module.part_2(f"{YEAR}/{DAY:0>2}/test.txt"))
print("Input:", module.part_2(f"{YEAR}/{DAY:0>2}/input.txt"))
