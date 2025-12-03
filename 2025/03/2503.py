def part_1(path: str):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()

    joltage = 0
    for line in lines:
        bank = [int(b) for b in line]
        i1, i2 = 0, 1
        bank_length = len(bank)
        for i, battery in enumerate(bank):
            if battery > bank[i1] and i < bank_length - 1:
                i1 = i
                i2 = i1 + 1
            if battery > bank[i2] or i2 <= i1:
                i2 = i

        bank_joltage = bank[i1] * 10 + bank[i2]
        joltage += bank_joltage

    return joltage


def part_2(path: str):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()

    joltage = 0
    n_batteries = 12
    for line in lines:
        bank = [int(b) for b in line]
        bank_length = len(bank)

        i_batteries_on = list(range(n_batteries))

        starting_i = 0
        for nth_battery in range(n_batteries):
            max_digit = 0
            for i in range(
                starting_i, bank_length - n_batteries + nth_battery + 1
            ):
                digit = bank[i]
                if digit > max_digit:
                    max_digit = digit
                    i_batteries_on[nth_battery] = i

            starting_i = i_batteries_on[nth_battery] + 1

            joltage += bank[i_batteries_on[nth_battery]] * pow(
                10, n_batteries - nth_battery - 1
            )

    return joltage
