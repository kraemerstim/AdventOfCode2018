aoc_input = open('2.input.txt', 'r')
lines = list(map(lambda x:x.strip(), aoc_input.readlines()))

def solve_2_1():
    threes = 0
    twos = 0
    for line in lines:
        two_found = False
        three_found = False

        used_chars = {}
        for char in line:
            if char in used_chars:
                used_chars[char] = used_chars[char]+1
            else:
                used_chars[char] = 1

        for x in used_chars.values():
            if x == 2:
                two_found = True
            if x == 3:
                three_found = True
        
        twos += 1 if two_found else 0
        threes += 1 if three_found else 0
    return twos * threes

def solve_2_2():
    for line1 in lines:
        for line2 in lines:
            position = -1
            difference_count = 0
            if line1 == line2: 
                continue
            for i in range(len(line1)):
                if not line1[i] == line2[i]:
                    difference_count += 1
                    position = i
            if difference_count == 1:
                return line1[:position] + line1[position+1:]


print('ergebnis 2_1: ' + str(solve_2_1()))
print('ergebnis 1_2: ' + str(solve_2_2()))