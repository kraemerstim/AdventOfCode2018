players = 411
last_marble_worth = 7205900

current_marble = None
next_available_marble = 1
current_player = 4
player_score = [0] * players

class DNode:
    def __init__(self, number):
        self.next = None
        self.prev = None
        self.number = number
    
    def get_prev_node(self, steps):
        current_node = self
        for i in range(steps):
            current_node = current_node.prev
        return current_node

    def get_next_node(self, steps):
        current_node = self
        for i in range(steps):
            current_node = current_node.next
        return current_node
    
    def set_side_nodes(self, left_node, right_node):
        left_node.next = self
        right_node.prev = self
        self.prev = left_node
        self.next = right_node

    def remove_from_circle(self):
        self.prev.next = self.next
        self.next.prev = self.prev

def initialize():
    global current_marble
    node = DNode(0)
    node.prev = node
    node.next = node
    current_marble = node

def take_turn():
    global current_marble
    global next_available_marble
    global current_player

    if next_available_marble % 23 == 0:
    
        additional_score = next_available_marble
        marble_to_remove = current_marble.get_prev_node(7)
        marble_to_remove.remove_from_circle()
        current_marble = current_marble.get_prev_node(6)
        additional_score += marble_to_remove.number
        player_score[current_player] += additional_score
    else:
        left_node = current_marble.get_next_node(1)
        right_node = current_marble.get_next_node(2)
        new_node = DNode(next_available_marble)
        new_node.set_side_nodes(left_node, right_node)
        current_marble = new_node

    next_available_marble += 1
    current_player = (current_player+1)%players

initialize()

while True:
    take_turn()
    if next_available_marble%100000 == 0:
        print(str((next_available_marble*100)/last_marble_worth))
    if next_available_marble > last_marble_worth:
        print(max(player_score))
        break