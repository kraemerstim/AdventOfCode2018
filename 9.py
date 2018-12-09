players = 10
last_marble_worth = 1618

current_marble_index = 1
marble_circle = [0, 4, 2, 1, 3]
next_available_marble = 5
current_player = 4
player_score = [0] * players

def take_turn():
    global marble_circle
    global current_marble_index
    global next_available_marble
    global current_player
    if next_available_marble % 23 == 0:
        player_score[current_player] += 23
    else:
        new_index = (current_marble_index+2)%len(marble_circle)
        marble_circle = marble_circle[:new_index] +[next_available_marble] + marble_circle[new_index:]
        current_marble_index = new_index
    next_available_marble += 1
    current_player = (current_player+1)%players

for i in range(28):
    take_turn()
    print(str(marble_circle) + ' ' + str(current_marble_index))

