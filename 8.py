from functools import reduce

numbers = list(map(lambda x:int(x), open('8.input.txt', 'r').readline().split(' ')))

class Node:
    def __init__(self):
        self.child_nodes = []
        self.metadata = []

def get_metadata_sum(index, metadatasum):
    child_count = numbers[index]
    metadata_count = numbers[index + 1]
    if child_count == 0:
        metadata_start_index = index + 2
        metadatasum += reduce(lambda x,y: x+y, numbers[metadata_start_index : metadata_start_index + metadata_count])
        return metadata_start_index + metadata_count, metadatasum
    index += 2
    for i in range(child_count):
        index, metadatasum = get_metadata_sum(index, metadatasum)
    metadatasum += reduce(lambda x,y: x+y, numbers[index : index + metadata_count])
    return index + metadata_count, metadatasum

def get_tree(index, this_node):
    child_count = numbers[index]
    metadata_count = numbers[index + 1]
    if child_count == 0:
        metadata_start_index = index + 2
        this_node.metadata = numbers[metadata_start_index : metadata_start_index + metadata_count]
        return metadata_start_index + metadata_count

    index += 2
    for i in range(child_count):
        temp_node = Node()
        this_node.child_nodes.append(temp_node)
        index = get_tree(index, temp_node)

    this_node.metadata = numbers[index : index + metadata_count]
    return index + metadata_count

def solve_8_2(node):
    temp_sum = 0
    if node.child_nodes == []:
        temp_sum = reduce(lambda x,y: x+y, node.metadata)
        return temp_sum
    for data in node.metadata:
        if data <= len(node.child_nodes):
            temp_sum += solve_8_2(node.child_nodes[data-1])
    return temp_sum 

index, metadatasum = get_metadata_sum(0,0)
print(metadatasum)

root = Node()
get_tree(0,root)
print(solve_8_2(root))