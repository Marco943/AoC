import re

re_times = re.compile("Time:([\d ]*)")
re_distances = re.compile("Distance:([\d ]*)")

with open("races.txt", "r") as f:
    races = f.read().strip()

    time = int(re_times.findall(races)[0].replace(" ", ""))
    distance = int(re_distances.findall(races)[0].replace(" ", ""))

speed = 0  # mm/s
acc = 1  # mm/s²


# race_n, race = 1, races[1]

time_limit = time
distance_to_beat = distance

times_held = range(0, time_limit)
n_times_won = 0
for time_held in times_held:
    # time_held = times_held[1]

    new_speed = speed + acc * time_held
    time_left = time_limit - time_held
    distance_traveled = new_speed * time_left
    if distance_traveled > distance_to_beat:
        n_times_won += 1

print(n_times_won)
