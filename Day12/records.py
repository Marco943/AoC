from functools import cache


def parse_line(line: str) -> tuple:
    records, groups = line.split(" ")
    records = "?".join([records] * 5)
    groups = tuple(map(int, groups.split(",") * 5))
    return (records, groups)


records = [
    parse_line(line)
    for line in open("Day12/records.txt", "r").read().strip().split("\n")
]


@cache
def parse_record(record: str, groups: tuple[int]) -> int:
    # print(record, groups)
    # Todos os grupos já foram preenchidos.
    if len(groups) == 0:
        # Se não tem mais mola na linha, VÁLIDO.
        if "#" not in record:
            return 1
        else:
            return 0

    # Acabou a linha mas ainda tem grupos a serem preenchidos, INVÁLIDO.
    if len(record) == 0:
        return 0

    # Caracter e grupos atuais
    cur_char = record[0]
    cur_group = groups[0]

    # Se houver menos caracteres disponíveis do que o grupo exige, INVÁLIDO.
    if len(record) < cur_group:
        return 0

    # Inicializa o contador de possibilidades
    out = 0

    # Se o caracter atual é um '.', não tem o que fazer e podemos pular para o próximo
    if cur_char in ".?":
        out += parse_record(record[1:], groups)

    # Se o caracter atual é um '#', analisamos se o grupo atual se encaixa
    if cur_char in "#?":
        this_group = record[:cur_group].replace("?", "#")
        # Verifica se há '#' o suficiente para se encaixar no grupo. Se não tiver, INVÁLIDO.
        if this_group != "#" * cur_group:
            out += 0

        elif len(record) == cur_group:
            if len(groups) == 1:
                out += 1
            else:
                out += 0
            # Se tiver, ainda verifica se o caracter após o grupo ainda é um '#'. Se for, INVÁLIDO.
        elif record[cur_group] in "?.":
            out += parse_record("." + record[cur_group + 1 :], groups[1:])

    return out


# for record in records:
possible = 0
for record in records:
    combinations = parse_record(*record)
    possible += combinations
    # print(record, combinations)
print("total:", possible)
