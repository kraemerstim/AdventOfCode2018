import re

order_pattern = 'Step (\w) must be finished before step (\w) can begin\.'

def parse_input(input_string):
    mo = re.search(order_pattern, input_string)
    if mo:
        x = mo.group(1)
        y = mo.group(2)
    return [x, y]

def create_lock_dict(orders):
    lock_dict = {}
    for order in orders:
        if order[0] not in lock_dict.keys():
            lock_dict[order[0]] = []
        if order[1] in lock_dict.keys():
            lock_dict[order[1]].append(order[0])
        else:
            lock_dict[order[1]] = [order[0]]
    return lock_dict

def get_todo_tasks(lock_dict):
    return_list = []
    for item in lock_dict.items():
        if item[1] == []:
            return_list.append(item[0])
    return return_list

def get_lowest_value(todo_tasks):
    s = 'Z'
    for item in todo_tasks:
        if ord(item) < ord(s):
            s = item
    return s

def delete_from_dict(s, lock_dict):
    if s in lock_dict:
        del lock_dict[s]
    for item in lock_dict.items():
        if s in item[1]:
            item[1].remove(s) 

orders = list(map(parse_input, open('7.input.txt', 'r').readlines()))

def solve_7_1():
    lock_dict = create_lock_dict(orders)
    todo_tasks = []
    result_string = ''
    while len(lock_dict) > 0:
        todo_tasks = get_todo_tasks(lock_dict)
        s = get_lowest_value(todo_tasks)
        result_string += s
        delete_from_dict(s, lock_dict)
    return result_string

def get_seconds_for_char(s):
    return ord(s) - ord('A') + 1 + 60

def fill_todo_tasks_with_seconds(lock_dict, work_tasks, queued_tasks):
    for item in lock_dict.items():
        if item[1] == [] and item[0] not in queued_tasks:
            found = False
            for work_task in work_tasks:
                if work_task[0] == item[0]:
                    found = True
                    break
            if not found:
                queued_tasks.append(item[0])

    queued_tasks.sort()
    for i in range(len(work_tasks), 5):
        if queued_tasks == []:
            break
        work_tasks.append([queued_tasks[0], get_seconds_for_char(queued_tasks[0])])
        queued_tasks.remove(queued_tasks[0])

    #print('lock_dict = ' + str(lock_dict))
    #print('work_tasks = ' + str(work_tasks))
    #print('queued_tasks = ' + str(queued_tasks))

def make_step_in_todo_tasks(todo_tasks):
    removed_list = []
    
    for i in range(len(todo_tasks)-1, -1, -1):
        task = todo_tasks[i]
        if task[1] > 1:
            task[1] -= 1
        else:
            removed_list.append(task[0])
            todo_tasks.remove(task)
    return removed_list
    

def solve_7_2():
    lock_dict = create_lock_dict(orders)
    queued_tasks = []
    work_tasks = []
    fill_todo_tasks_with_seconds(lock_dict, work_tasks, queued_tasks)
    seconds_used = 0
    while len(work_tasks) > 0:
        return_list = make_step_in_todo_tasks(work_tasks)
        while return_list == []:
            seconds_used += 1
            return_list = make_step_in_todo_tasks(work_tasks)
        seconds_used += 1
        for item in return_list:
            if item in lock_dict:
                delete_from_dict(item, lock_dict)
        fill_todo_tasks_with_seconds(lock_dict, work_tasks, queued_tasks)
        print('------')
        print(return_list)
        print(seconds_used)
        print(work_tasks)
        print(lock_dict)
        print('------')
    return seconds_used
        
def solve_7_2_debug():
    lock_dict = create_lock_dict(orders)
    queued_tasks = []
    work_tasks = []
    fill_todo_tasks_with_seconds(lock_dict, work_tasks, queued_tasks)
    print(lock_dict)
    print(work_tasks)
    print(queued_tasks)
    seconds_used = 0
    # while len(work_tasks) > 0:
    #     return_list = make_step_in_todo_tasks(work_tasks)
    #     while return_list == []:
    #         seconds_used += 1
    #         return_list = make_step_in_todo_tasks(work_tasks)
    #     seconds_used += 1
    #     fill_todo_tasks_with_seconds(lock_dict, work_tasks, queued_tasks)
    # return seconds_used


print(solve_7_1())
print(solve_7_2())