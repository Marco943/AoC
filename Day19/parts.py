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

print(rating)
