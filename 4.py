import re

guard_pattern = '\[.*\] Guard #(\d*) begins shift'
sleep_pattern = '\[.*:(\d*)\] falls asleep'
wake_pattern = '\[.*:(\d*)\] wakes up'

lines = list(map(lambda x: x.strip(), open('4.input.txt', 'r').readlines()))
lines.sort()

timetable = [{} for i in range(60)]

def solve_4_1():
    current_guard = -1
    sleep_time = 0
    guard_dict = {}
    max_sleeptime = 0
    max_sleepguard = 0
    for line in lines:
        guard = re.search(guard_pattern, line)
        sleep = re.search(sleep_pattern, line)
        wake = re.search(wake_pattern, line) 
        if guard:
            current_guard = int(guard.group(1))
            #print('guard = ' + guard.group(1))
        elif sleep:
            sleep_time = int(sleep.group(1))
            #print('sleep = ' + sleep.group(1))
        elif wake:
            #print('wake = ' + wake.group(1))
            wake_time = int(wake.group(1))
            for i in range(sleep_time, wake_time):
                if current_guard in timetable[i]:
                    timetable[i][current_guard] = timetable[i][current_guard] + 1
                else:
                    timetable[i][current_guard] = 1

            sleep_duration = wake_time - sleep_time
            if current_guard in guard_dict:
               guard_dict[current_guard] = guard_dict[current_guard] + sleep_duration
            else:
                guard_dict[current_guard] = sleep_duration
            if guard_dict[current_guard] > max_sleeptime:
                max_sleeptime = guard_dict[current_guard]
                max_sleepguard = current_guard

    print ('#' + str(max_sleepguard) + ': ' + str(max_sleeptime) + ' Minuten')

    max_sleep_current_guard = 0
    max_sleep_current_guard_minute = -1
    for i in range(60):
        if max_sleepguard in timetable[i]:
            if timetable[i][max_sleepguard] > max_sleep_current_guard:
                max_sleep_current_guard = timetable[i][max_sleepguard]
                max_sleep_current_guard_minute = i
    
    print('beste Minute: ' + str(max_sleep_current_guard_minute) + ' mit ' + str(max_sleep_current_guard) + ' Minuten')
    print('ergebnis 4_1: ' + str(max_sleep_current_guard_minute * int(max_sleepguard)))

    minute = 0
    guard = 0
    max_minute = 0
    for i in range(60):
        for key, value in timetable[i].items():
            if value > max_minute:
                max_minute = value
                guard = key
                minute = i
    
    print('ergebnis 4_2: ' + str(minute * guard))

solve_4_1()