import re

regexp = re.compile('position=<\s?([-]?\d*),\s*([ -]?\d*)> velocity=<\s?([-]?\d*),\s*([ -]?\d*)>')

class Star:
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
    
    def move_backwards(self):
        self.x -= self.vx
        self.y -= self.vy


def parse_code(pattern):
    m = regexp.match(pattern)
    result = list(map(lambda x: int(x), m.groups()))
    return Star(*result)

stars = list(map(parse_code, open('10.input.txt', 'r').readlines()))

def get_variance():
    min_x = stars[0].x
    max_x = stars[0].x
    min_y = stars[0].y
    max_y = stars[0].y
    for star in stars:
        if star.x < min_x:
            min_x = star.x
        if star.x > max_x:
            max_x = star.x
        if star.y < min_y:
            min_y = star.y
        if star.y > max_y:
            max_y = star.y     
    return (max_x, min_x, max_y, min_y)

def get_metric_variance():
    min_x, max_x, min_y, max_y = get_variance()
    return (max_x - min_x) * (max_y - min_y)


def do_turn():
    for star in stars:
        star.move()

def do_turn_backwards():
    for star in stars:
        star.move_backwards()

def print_text():
    max_x, min_x, max_y, min_y = get_variance()
    stars_array = [([' '] * (max_x - min_x + 1)) for i in range(max_y - min_y + 1)]
    for star in stars:
        stars_array[star.y-min_y][star.x-min_x] = 'X'
    for row in stars_array:
        print(row) 


old_variance = get_metric_variance()
seconds = 0
while True:
    do_turn()
    variance = get_metric_variance()
    if variance > old_variance:
        do_turn_backwards()
        print_text()
        print(seconds)
        break
    old_variance = variance
    seconds += 1
