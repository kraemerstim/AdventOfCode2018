tracks = list(map(lambda x: x.replace("\n", "") ,open("13.input.txt" , "r").readlines()))

class Car:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.next_intersection = "left"
    
    def is_in_same_place(self, car):
        if self.x == car.x and self.y == car.y:
            return True
        return False
    
    def move(self):
        if self.direction == "right":
            self.x += 1
        if self.direction == "left":
            self.x -= 1
        if self.direction == "up":
            self.y -= 1
        if self.direction == "down":
            self.y += 1

    def set_new_direction(self, new_char):
        if self.direction == "right":
            if new_char == "\\":
                self.direction = "down"
            if new_char == "/":
                self.direction = "up"
            if new_char == "+":
                if self.next_intersection == "left":
                    self.direction = "up"
                    self.next_intersection = "straight"
                elif self.next_intersection == "straight":
                    self.next_intersection = "right"
                elif self.next_intersection == "right":
                    self.direction = "down"
                    self.next_intersection = "left"
        elif self.direction == "left":
            if new_char == "\\":
                self.direction = "up"
            if new_char == "/":
                self.direction = "down"
            if new_char == "+":
                if self.next_intersection == "left":
                    self.direction = "down"
                    self.next_intersection = "straight"
                elif self.next_intersection == "straight":
                    self.next_intersection = "right"
                elif self.next_intersection == "right":
                    self.direction = "up"
                    self.next_intersection = "left"
        elif self.direction == "up":
            if new_char == "\\":
                self.direction = "left"
            if new_char == "/":
                self.direction = "right"
            if new_char == "+":
                if self.next_intersection == "left":
                    self.direction = "left"
                    self.next_intersection = "straight"
                elif self.next_intersection == "straight":
                    self.next_intersection = "right"
                elif self.next_intersection == "right":
                    self.direction = "right"
                    self.next_intersection = "left"
        elif self.direction == "down":
            if new_char == "\\":
                self.direction = "right"
            if new_char == "/":
                self.direction = "left"
            if new_char == "+":
                if self.next_intersection == "left":
                    self.direction = "right"
                    self.next_intersection = "straight"
                elif self.next_intersection == "straight":
                    self.next_intersection = "right"
                elif self.next_intersection == "right":
                    self.direction = "left"
                    self.next_intersection = "left"
        

def sort_cars(car):
    return car.x + car.y*200

def extract_cars():
    cars = []
    for i, track in enumerate(tracks):
        index = track.find("v")
        while index > -1:
            cars.append(Car(index, i, "down"))
            index = track.find("v", index+1)
        index = track.find("^")
        while index > -1:
            cars.append(Car(index, i, "up"))
            index = track.find("^", index+1)
        index = track.find("<")
        while index > -1:
            cars.append(Car(index, i, "left"))
            index = track.find("<", index+1)
        index = track.find(">")
        while index > -1:
            cars.append(Car(index, i, "right"))
            index = track.find(">", index+1)
    return cars

def remove_vehicles_from_tracks():
    return list(map(remove_vehicles_from_track, tracks))

def car_in_same_place(car, cars):
    for temp_car in cars:
        if temp_car is car:
            continue
        if car.is_in_same_place(temp_car):
            return True
    return False

def remove_vehicles_from_track(track):
    track = track.replace("v", "|")
    track = track.replace("^", "|")
    track = track.replace(">", "-")
    track = track.replace("<", "-")
    return track

cars = extract_cars()
tracks = remove_vehicles_from_tracks()
crash_cars = []
while True:
    cars.sort(key=sort_cars)
    for car in crash_cars:
        cars.remove(car)
    crash_cars = []
    if len(cars) == 1:
        print('last car: ' + str(cars[0].x) + ' ' + str(cars[0].y))
        exit()
    for car in cars:
        if car in crash_cars:
            continue
        car.move()
        car.set_new_direction(tracks[car.y][car.x])
        if (car_in_same_place(car, cars)):
            print(str(car.x) + ' ' + str(car.y))
            for crash_car in cars:
                if crash_car.x == car.x and crash_car.y == car.y:
                    crash_cars.append(crash_car)
            