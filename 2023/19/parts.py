import os
import re

os.chdir("Day19")
file = open("parts.txt", "r").read().strip().split("\n\n")

re_wf_name = re.compile(r"([a-z]*){")
re_wf_conditions = re.compile(r"([xmas]{1}[><]{1}\d*):([a-zA-Z]+)")
re_wf_default = re.compile(r",([a-zA-Z]+)}$")
re_pt_values = re.compile(r"([xmas]{1})=(\d+)")

workflows = {}
for line in file[0].split("\n"):
    name = re_wf_name.findall(line)[0]
    conditions = re_wf_conditions.findall(line)
    default = re_wf_default.findall(line)[0]
    workflows[name] = {"conds": conditions, "dft": default}

parts = []
for line in file[1].split("\n"):
    values = re_pt_values.findall(line)
    values = {k: int(v) for k, v in values}
    parts.append(values)

# PART 1
rating = 0
for part in parts:
    accepted = False
    x, m, a, s = part["x"], part["m"], part["a"], part["s"]
    cur_wf = "in"
    while True:
        cur_conds = workflows[cur_wf]["conds"]
        for cond in cur_conds:
            if eval(cond[0]):
                next_wf = cond[1]
                break
        else:
            next_wf = workflows[cur_wf]["dft"]
        if next_wf == "A":
            accepted = True
            break
        elif next_wf == "R":
            break
        else:
            cur_wf = next_wf

    if accepted:
        rating += x + m + a + s

print("PART 1:", rating)


# PART 2
def calc_combs(ranges: dict[str, tuple]) -> int:
    combs = 1
    for min, max in ranges.values():
        if max > min:
            combs *= max - min + 1
    if combs == 1:
        return 0
    return combs


def workflow(ranges: dict[str, tuple], cur_wf) -> int:
    conds = workflows[cur_wf]["conds"]
    default = workflows[cur_wf]["dft"]
    combs = 0

    for cond_eval, cond_wf in conds:
        passed_ranges = dict(ranges)
        denied_ranges = dict(ranges)

        if "<" in cond_eval:
            var, cut_val = cond_eval.split("<")
            passed_ranges[var] = (passed_ranges[var][0], int(cut_val) - 1)
            denied_ranges[var] = (int(cut_val), denied_ranges[var][1])

        else:
            var, cut_val = cond_eval.split(">")
            passed_ranges[var] = (int(cut_val) + 1, passed_ranges[var][1])
            denied_ranges[var] = (denied_ranges[var][0], int(cut_val))

        if cond_wf == "A":
            combs += calc_combs(passed_ranges)
        elif cond_wf != "R":
            combs += workflow(passed_ranges, cond_wf)

        ranges = denied_ranges

    if default == "A":
        combs += calc_combs(ranges)
    elif default != "R":
        combs += workflow(ranges, default)
    return combs


ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}

print("PART 2:", workflow(ranges, "in"))
