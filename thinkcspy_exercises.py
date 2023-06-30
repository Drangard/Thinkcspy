import math
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
        average_speed(self)


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
        print(radius)

    def two_2(self):
        cover_price = float(24.95)
        store_discount = .40
        num_copies = 60
        shipping_cost = ((num_copies - 1) * .75) + 3
        discounted_cover_price = cover_price * store_discount
        total_cover_price = num_copies * discounted_cover_price
        wholesale_cost = total_cover_price + shipping_cost
        print(wholesale_cost) 

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
        print(int(arrival_hours), ':', int(arrival_minuntes))

chapter2 = Chapter_2()
#chapter2.one_1()
#chapter2.two_1()
#chapter2.two_2()
#chapter2.two_3()

class Chapter_3():
    def one_1():
        pass