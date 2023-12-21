import os
from collections import deque

os.chdir("Day20")
lines: list[str] = open("pulses.txt", "r").read().strip().split("\n")

modules: dict[str, dict] = {}
for line in lines:
    module, dests = line.split(" -> ")
    match module[0]:
        case "%":
            mod_type = "ff"
            mod_name = module[1:]
        case "&":
            mod_type = "co"
            mod_name = module[1:]
        case _:
            mod_type = ""
            mod_name = module
    dests = tuple(map(str.strip, dests.split(",")))
    modules[mod_name] = {"type": mod_type, "dests": dests, "st": False, "pulse": -1}
    if mod_type == "co":
        modules[mod_name]["recent"] = {}

for name, module in modules.items():
    if module["type"] != "co":
        continue
    for name_input, module_input in modules.items():
        if name in module_input["dests"]:
            modules[name]["recent"][name_input] = -1


def are_all_ff_off(modules: dict[str, dict]):
    ff_modules_st = [
        module["st"] for _, module in modules.items() if module["type"] == "ff"
    ]
    return not any(ff_modules_st)


high_pulses = 0
low_pulses = 0

for i in range(1000):
    modules_handle: deque = deque(["broadcaster"])
    low_pulses += 1
    while True:
        if not modules_handle:
            break
        cur = modules_handle.popleft()
        if cur not in modules:
            continue
        dests = modules[cur]["dests"]

        for dest in dests:
            if modules[cur]["pulse"] == 1:
                high_pulses += 1
            else:
                low_pulses += 1
            # print(cur, modules[cur]["pulse"], "->", dest)
            if dest not in modules:
                continue
            if modules[dest]["type"] == "ff":
                if modules[cur]["pulse"] == 1:
                    continue
                elif modules[cur]["pulse"] == -1:
                    if modules[dest]["st"]:
                        modules[dest]["pulse"] = -1
                    else:
                        modules[dest]["pulse"] = 1
                    modules[dest]["st"] = not modules[dest]["st"]
                    modules_handle.append(dest)

            elif modules[dest]["type"] == "co":
                modules[dest]["recent"][cur] = modules[cur]["pulse"]
                if all(map(lambda x: x == 1, modules[dest]["recent"].values())):
                    modules[dest]["pulse"] = -1
                else:
                    modules[dest]["pulse"] = 1
                modules_handle.append(dest)


print("High:", high_pulses, "Low:", low_pulses)
print("PARTE 1:", high_pulses * low_pulses)
