from string import ascii_lowercase
inputstring = open('5.input.txt', 'r').readline()

#inputstring = 'aAbBccDdEEFf'

def react(inputstring):
    found = True
    while found == True:
        found = False
        max_letters = len(inputstring)
        for i in range(max_letters, -1, -1):
            if i >= len(inputstring)-1:
                continue
            if abs(ord(inputstring[i+1])-ord(inputstring[i])) == 32:
                inputstring = inputstring[:i] + inputstring[i+2:]
                found = True
    return inputstring

def solve_5_1():
    return len(react(inputstring))

def solve_5_2():
    lowest_count = -1
    for character in ascii_lowercase:
        new_string = inputstring.replace(character, '')
        new_string = new_string.replace(chr(ord(character)-32), '')
        new_string = react(new_string)
        if lowest_count == -1 or len(new_string) < lowest_count:
            lowest_count = len(new_string)
    return lowest_count

print('Lösung für 5.1: ' + str(solve_5_1()))
print('Lösung für 5.2: ' + str(solve_5_2()))