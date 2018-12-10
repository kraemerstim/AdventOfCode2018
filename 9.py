players = 411
last_marble_worth = 72059

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
        additional_score = next_available_marble
        remove_marble_index = (current_marble_index-7)%len(marble_circle)
        additional_score += marble_circle[remove_marble_index]
        marble_circle = marble_circle[:remove_marble_index] + marble_circle[remove_marble_index+1:]
        current_marble_index = (remove_marble_index)%len(marble_circle)
        player_score[current_player] += additional_score
        #print(str(next_available_marble) + ': ' + str(additional_score) + ' ... ' + str(player_score))
    else:
        new_index = (current_marble_index+2)%len(marble_circle)
        marble_circle = marble_circle[:new_index] +[next_available_marble] + marble_circle[new_index:]
        current_marble_index = new_index
    next_available_marble += 1
    current_player = (current_player+1)%players

while True:
    take_turn()
    if next_available_marble > last_marble_worth:
        print(max(player_score))
        break

#for i in range(2000):
#    take_turn()
#    print(str(marble_circle) + ' ' + str(current_marble_index))

