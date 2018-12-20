puzzle_input = 327901
puzzle2_input = [3,2,7,9,0,1]

recepies = [3,7,1,0,1,0]

current_index = [3,4]

while True: #len(recepies) < (puzzle_input + 10):
    values = [recepies[current_index[0]], recepies[current_index[1]]]
    value_sum = values[0] + values[1]
    if value_sum  > 9:
        recepies.append(1)
    recepies.append(value_sum%10)
    current_index[0] = (current_index[0] + values[0] + 1)%len(recepies)
    current_index[1] = (current_index[1] + values[1] + 1)%len(recepies)

    if(recepies[-6:] == puzzle2_input):
        print(len(recepies)-6)
        break
    if(recepies[-7:-1] == puzzle2_input):
        print(len(recepies)-7)
        break
    if(len(recepies)%10000 == 0):
        print(len(recepies))