import turtle
import random
        
        
class CreatePolygon:
    def __init__(self, num_sides, embeded):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-248, 249), random.randint(-159, 159)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = 0.618
        self.embeded = embeded
    def draw_polygon(self):
        turtle.colormode(255)
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for i in range(self.embeded):
            for _ in range(self.num_sides):
                turtle.forward(self.size)
                turtle.left(360/self.num_sides)
            self.reposition()
            self.size *= self.reduction_ratio
        turtle.penup()
        
    def reposition(self):
        turtle.penup()
        turtle.forward(self.size*(1-self.reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-self.reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        turtle.pendown()
        
class CreateArtWork:
    def __init__(self, pattern):
        self.pattern = pattern
        
    def create_art_work(self):
        turtle.speed(10)
        turtle.bgcolor('black')
        polygon_amount = random.randint(15, 20)
        if self.pattern == 1:
            for i in range(polygon_amount):
                art1 = CreatePolygon(3, 1)
                art1.draw_polygon()
        elif self.pattern == 2:
            for i in range(polygon_amount):
                art1 = CreatePolygon(4, 1)
                art1.draw_polygon()
        elif self.pattern == 3:
            for i in range(polygon_amount):
                art1 = CreatePolygon(5, 1)
                art1.draw_polygon()
        elif self.pattern == 4:
            for i in range(polygon_amount):
                art1 = CreatePolygon(random.randint(3,5), 1)
                art1.draw_polygon()
        elif self.pattern == 5:
            for i in range(polygon_amount):
                art1 = CreatePolygon(3, 3)
                art1.draw_polygon()
        elif self.pattern == 6:
            for i in range(polygon_amount):
                art1 = CreatePolygon(4, 3)
                art1.draw_polygon()
        elif self.pattern == 7:
            for i in range(polygon_amount):
                art1 = CreatePolygon(5, 3)
                art1.draw_polygon()
        elif self.pattern == 8:
            for i in range(polygon_amount):
                art1 = CreatePolygon(random.randint(3,5), 3)
                art1.draw_polygon()
        elif self.pattern == 9:
            print(self.pattern)
            for i in range(polygon_amount):
                randomEmbeded = random.randint(1,3)
                if randomEmbeded == 2:
                    randomEmbeded = random.randint(1,3)
                art1 = CreatePolygon(random.randint(3,5), randomEmbeded)
                art1.draw_polygon()
        turtle.hideturtle()
        turtle.done()

pattern = int(input("Please enter number of art pattern(1-9) you would like to see: "))
shape1 = CreateArtWork(pattern)
shape1.create_art_work()
