import re

aoc_input = open('3.input.txt', 'r')
lines = list(map(lambda x: x.strip(), aoc_input.readlines()))
regexp = re.compile('#(\d*) @ (\d*),(\d*): (\d*)x(\d*)')

def parse_code(pattern):
    m = regexp.match(pattern)
    result = list(map(lambda x: int(x), m.groups()))
    return result

def get_pattern_size():
    h = 0
    w = 0
    for line in lines:
        l = parse_code(line)
        temp_h = l[4] + l[2]
        temp_w = l[3] + l[1]
        h = temp_h if temp_h > h else h
        w = temp_w if temp_w > w else w
    return w, h


def solve_3_1():
    w, h = get_pattern_size()
    pattern = [[0] * w for i in range(h)]
    inches_overlapped = 0
    for line in lines:
        results = parse_code(line)
        r_left = results[1]
        r_top = results[2]
        r_width = results[3]
        r_height = results[4]
        for x in range(r_left, r_left + r_width):
            for y in range(r_top, r_top + r_height):
                if pattern[y][x] == 0:
                    pattern[y][x] = 1
                elif pattern[y][x] == 1:
                    pattern[y][x] = 2
                    inches_overlapped += 1

    return inches_overlapped

def solve_3_2():
    w, h = get_pattern_size()
    pattern = [[0] * w for i in range(h)]
    inches_overlapped = 0
    for line in lines:
        results = parse_code(line)
        for x in range(results[1], results[1] + results[3]):
            for y in range(results[2], results[2] + results[4]):
                if pattern[y][x] == 0:
                    pattern[y][x] = 1
                elif pattern[y][x] == 1:
                    pattern[y][x] = 2
                    inches_overlapped += 1

    for line in lines:
        results = parse_code(line)
        overlapped = False
        for x in range(results[1], results[1] + results[3]):
            if overlapped:
                break
            for y in range(results[2], results[2] + results[4]):
                if pattern[y][x] == 2:
                    overlapped = True
                    break
        if not overlapped:
            return results[0]


print(str(solve_3_1()))
print(str(solve_3_2()))