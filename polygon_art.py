import turtle
import random


class Draw_Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Run:
    def __init__(self):
        self.choice = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive: "))
        self.num = int(input("How many do you want: "))

    def main(self):
        if self.choice == 1:
            for _ in range(self.num):
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)

                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = 3  # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                i = Draw_Polygon(num_sides, size, orientation, location, color, border_size)

                # specify a reduction ratio to draw a smaller polygon inside the one above
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original
                Draw_Polygon.draw_polygon(i)

            # hold the window; close it by clicking the window close 'x' mark
            turtle.done()

        elif self.choice == 2:
            for _ in range(self.num):
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)

                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = 4  # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                i = Draw_Polygon(num_sides, size, orientation, location, color, border_size)

                # specify a reduction ratio to draw a smaller polygon inside the one above
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original
                Draw_Polygon.draw_polygon(i)

            # hold the window; close it by clicking the window close 'x' mark
            turtle.done()


        elif self.choice == 3:
            for _ in range(self.num):
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)

                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = 5  # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                i = Draw_Polygon(num_sides, size, orientation, location, color, border_size)

                # specify a reduction ratio to draw a smaller polygon inside the one above
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original
                Draw_Polygon.draw_polygon(i)

            # hold the window; close it by clicking the window close 'x' mark
            turtle.done()


        elif self.choice == 4:
            for _ in range(self.num):
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)

                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = random.randint(3,5)  # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                i = Draw_Polygon(num_sides, size, orientation, location, color, border_size)

                # specify a reduction ratio to draw a smaller polygon inside the one above
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original
                Draw_Polygon.draw_polygon(i)

            # hold the window; close it by clicking the window close 'x' mark
            turtle.done()



        elif self.choice == 5:
            for _ in range(self.num):
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)

                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = 3  # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                i = Draw_Polygon(num_sides, size, orientation, location, color, border_size)

                # specify a reduction ratio to draw a smaller polygon inside the one above
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original
                Draw_Polygon.draw_polygon(i)

            # hold the window; close it by clicking the window close 'x' mark
            turtle.done()


        elif self.choice == 6:
            for _ in range(self.num):
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)

                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = 4  # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                i = Draw_Polygon(num_sides, size, orientation, location, color, border_size)

                # specify a reduction ratio to draw a smaller polygon inside the one above
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original
                Draw_Polygon.draw_polygon(i)

            # hold the window; close it by clicking the window close 'x' mark
            turtle.done()


        elif self.choice == 7:
            for _ in range(self.num):
                turtle.speed(0)
                turtle.bgcolor('black')
                turtle.tracer(0)
                turtle.colormode(255)

                # draw a polygon at a random location, orientation, color, and border line thickness
                num_sides = 5  # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                border_size = random.randint(1, 10)
                i = Draw_Polygon(num_sides, size, orientation, location, color, border_size)

                # specify a reduction ratio to draw a smaller polygon inside the one above
                reduction_ratio = 0.618

                # reposition the turtle and get a new location
                turtle.penup()
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(size * (1 - reduction_ratio) / 2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]

                # adjust the size according to the reduction ratio
                size *= reduction_ratio

                # draw the second polygon embedded inside the original
                Draw_Polygon.draw_polygon(i)

            # hold the window; close it by clicking the window close 'x' mark
            turtle.done()



start = Run()
start.main()