import time
from argparse import ArgumentParser
from importlib import import_module

arg_parser = ArgumentParser()
arg_parser.add_argument("-y", "--year", required=True)
arg_parser.add_argument("-d", "--day", required=True)
arg_parser.add_argument("-t", "--test", required=False, action="store_true")

args = arg_parser.parse_args()

YEAR: int = args.year
DAY: int = args.day
TEST = args.test


def timeit(funcao):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        r = funcao(*args, **kwargs)
        dt = time.time() - t1
        return f"[{dt*1000:.2f} ms] {r}"

    return wrapper


module = import_module(f"{YEAR}.{DAY:0>2}.{YEAR[-2:]}{DAY:0>2}")

print("=" * 20 + " PART 1 " + "=" * 20)
print("[Test]", timeit(module.part_1)(f"{YEAR}/{DAY:0>2}/test.txt"))
if not TEST:
    print("[Input]", timeit(module.part_1)(f"{YEAR}/{DAY:0>2}/input.txt"))
print("=" * 20 + " PART 2 " + "=" * 20)
print("[Test]", timeit(module.part_2)(f"{YEAR}/{DAY:0>2}/test.txt"))
if not TEST:
    print("[Input]", timeit(module.part_2)(f"{YEAR}/{DAY:0>2}/input.txt"))
