import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

        
    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)
        
    def level_up(self):
        self.move_distance += MOVE_INCREMENT
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)
    pass
