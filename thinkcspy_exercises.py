from __future__ import print_function, division
import math
from time import time
import turtle


class Chapter_1():
    def one_1(self):
        print('1.1.1 >> Hello World!')
        #what happenes when you leave out a parenteses
        #print('Hello world'
    def one_2(self):
        print("1.1.2 >> Hello world!")
        #what happens if you leave out one or both quotation marks
        #print(hello world)        
        #print('hello world)
        #print(hello world")
        #print(hello world")
    def one_3(self):
        print("1.1.3 >>", 2+-2,', ', 2+2,", ", 2++2,", ", 2++3)

    def one_4(self):
        #check how many leading zeros you can have in math notation
        #print(2 + 02)
        pass
    
    def one_5(self):
        #if you put 2 values together with no operator
        #print(7 8)
        pass
    
    def two_1(self):
        def Counting_seconds(self):
            seconds = 1
            minutes = 60 * seconds
            time = (42 * minutes) + (42 * seconds)
            print("1.2.1 >>", time)
        Counting_seconds(self)

    def two_2(self):
        def How_many(self):
            kilometers = 10
            miles = kilometers * .62
            print('1.2.2 >>',float(miles))
        How_many(self)

    def two_3(self):
        def average_speed(self):
            kilometers = 10
            miles = kilometers * .62
            conversion = 10 * miles
            seconds = 42
            minutes = 42
            hours =  (minutes + seconds / 60) / 60
            pace = miles / hours
            print("1.2.3 >>", pace)
        average_speed()

chapter1 = Chapter_1()
# Erase (#) to check answer
#chapter1.one_1()
#chapter1.one_2()
#chapter1.one_3()
#chapter1.one_4()
#chapter1.one_5()
#chapter1.two_1()
#chapter1.two_2()
#chapter1.two_3()


class Chapter_2():
    def one_1(self):
        # Playing with errors
        #a = n - 42
        #a = 42 - n
        #a = x - y - 1
        #a = 12:
        #a = 1.
        #a = xy
        pass
    def two_1(self):
        r = 5
        radius = ((4/3) * math.pi * (r ** 3))
        print('2.2.1 >>', radius)

    def two_2(self):
        cover_price = float(24.95)
        store_discount = .40
        num_copies = 60
        shipping_cost = ((num_copies - 1) * .75) + 3
        discounted_cover_price = cover_price * store_discount
        total_cover_price = num_copies * discounted_cover_price
        wholesale_cost = total_cover_price + shipping_cost
        print('2.2.2 >>', wholesale_cost) 
    def two_3(self):
        start_time_minutes = (6 * 60) + 52
        easy_pace_minutes = 8
        easy_pace_seconds = 15
        tempo_minuts = 7
        tempo_seconds = 12
        easy_pace_total = 2 * (easy_pace_minutes + easy_pace_seconds / 60)
        tempo_pace_total = 3 * (tempo_minuts + tempo_seconds / 60)
        arrival_time_minutes = start_time_minutes + easy_pace_total + tempo_pace_total
        arrival_hours = arrival_time_minutes // 60
        arrival_minuntes = arrival_time_minutes % 60
        print('2.2.3 >>', int(arrival_hours), ':', int(arrival_minuntes))

chapter2 = Chapter_2()
#chapter2.one_1()
#chapter2.two_1()
#chapter2.two_2()
#chapter2.two_3()

class Chapter_3():
    def one_1(self):
        def right_justify(self):
            name = "monty python"
            result = name.rjust(17, ' ')
            print('3.1.1 >> ', result)
        right_justify()

    def two_1(self):
        def do_twice(f):
            f(self)
            f(self)
        def print_monty(self):
            print('3.2.1')
            print('monty python')
        do_twice(print_monty)

    def two_2(self):
        def print_twice():
            print('spam')
            print('spam')
        print_twice()

    def two_3(self):
        def print_twice():
            print('spam')
            print('spam')

        def do_twice(f):
            f()
            f()
        print('3.2.3')
        do_twice(print_twice)

    def two_4(self):
        def print_twice():
            print('spam')
            print('spam')

        def do_twice(f):
            f()
            f()

        def do_four():
            do_twice(print_twice)
            do_twice(print_twice)
        print('3.2.4 >>')
        do_four()

    def three_1(self):

        def do_twice(f):
            f()
            f()

        def do_four(f):
            do_twice(f)
            do_twice(f)

        def print_beam():
            print('+ - - - -', end=' ')

        def print_post():
            print ('|        ', end=' ')

        def print_beams():
            do_twice(print_beam)
            print('+')

        def print_posts():
            do_twice(print_post)
            print('|')

        def print_row():
            print_beams()
            do_four(print_posts)

        def print_grid():
            do_twice(print_row)
            print_beams()

        print('3.3.1 >>')
        print_grid()

    def three_2(self):

        def do_twice(f):
            f()
            f()

        def do_four(f):
            do_twice(f)
            do_twice(f)

        def print_beam():
            print('+ - - - -', end=' ')

        def print_post():
            print ('|        ', end=' ')

        def print_beams():
            do_twice(print_beam)
            print('+')

        def print_posts():
            do_twice(print_post)
            print('|')

        def print_row():
            print_beams()
            do_four(print_posts)

        def print_grid():
            do_twice(print_row)
            print_beams()


        def print_grid_twice():
            do_twice(print_grid)
        print('3.3.2 >>')
        print_grid_twice()
        #print('if you see this tell endless')

chapter3 = Chapter_3()
#chapter3.one_1()
#chapter3.two_1()
#chapter3.two_2()
#chapter3.two_3()
#chapter3.two_4()
#chapter3.two_5()
#chapter3.three_1()
#chapter3.three_2()

class Chapter_4():
    def two_1():
        #involves turtle cant do it yet
        t = turtle.Turtle()
        t.speed(10)
        turtle.bgcolor("blue")
        colors = ["red", 'green', 'white']
        t.shape('turtle')
    
        for i in range(36):
            t.color(colors[i % len(colors)])
            t.forward(100)
            t.left(45)
            t.forward(100)
            t.left(135)
            t.forward(100)
            t.left(45)
            t.forward(100)
            t.left(135)
            t.right(10)

        t.hideturtle()
        turtle.mainloop()

    def three_1():
        def draw_pie(t, n, r):

            pie(t, n, r)
            t.penup()
            t.forward(r*2 + 10)
            t.pendown()


        def pie(t, n, r):

            angle = 360.0 / n
            for i in range(n):
                triangle(t, r, angle/2)
                t.left(angle)


        def triangle(t, r, angle):
            y = r * math.sin(angle * math.pi / 180)

            t.right(angle)
            t.forward(r)
            t.left(90+angle)
            t.forward(2*y)
            t.left(90+angle)
            t.forward(r)
            t.left(180-angle)


        link = turtle.Turtle()

        link.penup()
        link.back(130)
        link.pendown()

        size = 40
        draw_pie(link, 9, size)

    def four_1():
        #have to draw the alphabet int turtle
        pass

    def five_1():
        def spiral():
            t = turtle.Turtle()
            t.speed(10)
            t.penup()
            t.goto(-100, 0)
            t.pendown()
            side_length = 1
            next_side_length = 1
            angle = 90
            next_angle = 90

            while side_length < 1000:
                t.forward(side_length)
                t.right(angle)
                temp = next_side_length
                next_side_length = side_length + next_side_length
                side_length = temp

                angle = 180 - ((180 * next_angle) / (angle + next_angle))
                next_angle = 180 - angle
            turtle.mainloop()
        spiral()

    

chapter4 = Chapter_4
#chapter4.two_1()
#chapter4.three_1()
#chapter4.four_1()
chapter4.five_1()
        

class Chapter_5():
    def one_1(self):
        pass
