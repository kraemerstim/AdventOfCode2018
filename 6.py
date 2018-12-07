import re

coordinate_pattern = '^(\d*), (\d*)'

def parse_numbers(input_string):
    mo = re.search(coordinate_pattern, input_string)
    if mo:
        x = int(mo.group(1))
        y = int(mo.group(2))
    return [x, y]

def find_min_max_x_y(coordinates):
    min_x = coordinates[0][0]
    min_y = coordinates[0][1]
    max_x = coordinates[0][0]
    max_y = coordinates[0][1]
    for coordinate in coordinates:
        if coordinate[0] < min_x:
            min_x = coordinate[0]
        elif coordinate[0] > max_x:
            max_x = coordinate[0]
        if coordinate[1] < min_y:
            min_y = coordinate[1]
        elif coordinate[1] > max_y:
            max_y = coordinate[1]
    return [[min_x, min_y],[max_x, max_y]]

def get_manhatten_distance(c_from, c_to):
    return abs(c_from[0] - c_to[0]) + abs(c_from[1] - c_to[1])

def generate_pattern(coordinates, mmc):
    pattern = [[[-1, 0]] * (mmc[1][0]+1) for i in range(mmc[1][1]+1)]
    index = 0
    for coordinate in coordinates:
        for i in range(mmc[0][0], mmc[1][0]+1):
            for j in range(mmc[0][1], mmc[1][1]+1):
                distance = get_manhatten_distance(coordinate, [i,j])
                if (pattern[j][i][0] == -1) or (pattern[j][i][1] > distance):
                    pattern[j][i] = [index, distance]
                elif pattern[j][i][1] == distance:
                    pattern[j][i] = [-2, distance]
        index+=1
    return pattern

def generate_infinity_list(pattern, mmc):
    infinite_list = []
    #=
    for i in range(mmc[0][0], mmc[1][0]+1):
        index = pattern[mmc[0][1]][i][0]
        if not pattern in infinite_list:
            infinite_list.append(index)
        index = pattern[mmc[1][1]][i][0]
        if not pattern in infinite_list:
            infinite_list.append(index)
    #||
    for i in range(mmc[0][1], mmc[1][1]+1):
        index = pattern[i][mmc[0][0]][0]
        if not pattern in infinite_list:
            infinite_list.append(index)
        index = pattern[i][mmc[1][0]][0]
        if not pattern in infinite_list:
            infinite_list.append(index)
    
    return infinite_list

def get_max_area(pattern, infinity_list, mmc):
    max_count = 0
    for i in range(len(coordinates)+ 1):
        if i in infinity_list:
            continue
        current_count = 0
        for x in range(mmc[0][0], mmc[1][0]):
            for y in range(mmc[0][1], mmc[1][1]):
                if pattern[y][x][0] == i:
                    current_count += 1
        if current_count > max_count:
            max_count = current_count

    return max_count

def get_combined_distance(coordinate, coordinates):
    sum_distance = 0
    for c in coordinates:
        sum_distance += get_manhatten_distance(c, coordinate)
    return sum_distance

def solve_6_1():
    mmc = find_min_max_x_y(coordinates)
    pattern = generate_pattern(coordinates, mmc)
    infinity_list = generate_infinity_list(pattern, mmc)
    return get_max_area(pattern, infinity_list, mmc)

def solve_6_2():
    mmc = find_min_max_x_y(coordinates)
    fieldcount = 0
    for x in range(mmc[0][0], mmc[1][0]):
        for y in range(mmc[0][1], mmc[1][1]):
            if get_combined_distance([x,y], coordinates) < 10000:
                fieldcount += 1
    return fieldcount


coordinates = list(map(parse_numbers, open('6.input.txt', 'r').readlines()))
print(solve_6_1())
print(solve_6_2())