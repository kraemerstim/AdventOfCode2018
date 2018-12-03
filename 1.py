aoc_input = open('1.input.txt', 'r')
lines = list(map(lambda x: x.strip(), aoc_input.readlines()))

def solve_1_1():
    i = 0
    for line in lines:
        i += int(line)
    return i

def solve_1_2():
    i = 0
    used_values = set()
    while True:
        for line in lines:
            i += int(line)

            if i in used_values:
                return i
            else:
                used_values.add(i)

def solve_1_2b():
    liste = []
    i = 0
    for line in lines:
        i += int(line)
        if i in liste:
            return i
        liste.append(i)

    modulo_value = i

    difference = -1
    result = 0
    for i in range(len(liste)):
        for j in range(len(liste)):
            if i == j:
                continue
            v1 = liste[i]
            v2 = liste[j]
            if v1 > v2:
                continue
            if not v1%modulo_value == v2%modulo_value:
                continue
            if (difference == -1) or (v2 - v1 < difference):
                difference = v2 - v1
                result = v2
    if difference > -1:
        return result
    if modulo_value == 0:
        return liste[0]
    return 'kein Ergebnis'
            


print('ergebnis 1_1: ' + str(solve_1_1()))
print('ergebnis 1_2: ' + str(solve_1_2()))
print('ergebnis 1_2b: ' + str(solve_1_2b()))