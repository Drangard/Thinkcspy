from __future__ import print_function, division
text_file = 'words.txt'
import math
import datetime
import turtle
import random
import sys

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

            while side_length < 100:
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
#chapter4.five_1()
        
class Chapter_5():
    def one_1():
        def clock():
            current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
            print(current_time)
        clock()

    def two_1():
        def fermats_last_theorem(a, b, c, n):
            if n > 2 and a ** n + b ** n == c ** n:
                print('Holy smokes, Fermat was wrong!')
            else:
                print("No, that doesn’t work.")

        a = int(input('what is a?'))
        b = int(input('what is b?'))
        c = int(input('what is c?'))
        n = int(input('what is n?'))

        fermats_last_theorem(a, b, c, n)

    def three_1():
        def is_triangle(a, b, c):
            if a + b > c and b + c > a and c + a > b:
                return True
            else:
                return False
    
        stick_a = float(input('Input stick a.'))
        stick_b = float(input('Input stick b.'))
        stick_c = float(input('Input stick c.'))

        if is_triangle(stick_a, stick_b, stick_c):
            print('they can form a triangle.')
        else:
            print('they cannot make a triangle.')

    def six_1():
        def koch_curve(t, length, depth):
            if depth == 0:
                t.forward(length)
            else:
                koch_curve(t, length / 3, depth - 1)
                t.left(60)
                koch_curve(t, length / 3, depth - 1)
                t.right(120)
                koch_curve(t, length / 3, depth - 1)
                t.left(60)
                koch_curve(t, length / 3, depth - 1)

        def snowflake(t, length, depth):
            for i in range(3):
                koch_curve(t, length, depth)
                t.right(120)

        t = turtle.Turtle()
        t.speed(100)

        t.penup()
        t.goto(-200, 75)
        t.pendown()
        snowflake(t, 400, 4)
        turtle.done()

chapter5 = Chapter_5
#chapter5.one_1()
#chapter5.two_1()
#chapter5.three_1()
#chapter5.six_1()

class Chapter_6():

    def two_1():
        def ackermann_func(m, n):
            if m == 0:
                return n + 1
            elif m > 0 and n == 0:
                return ackermann_func(m - 1, 1)    
            elif m > 0 and n > 0:
                return ackermann_func(m - 1, ackermann_func(m, n - 1))
        
        num_1 = float(input('Enter first number. >>>'))
        num_2 = float(input('Enter second number. >>>'))

        print(ackermann_func(num_1, num_2))

    def three_2():
        def convert_to_lowercase(string):
            lowercase_string = ""
            for char in string:
                if char.isupper():
                    lowercase_string += char.lower()
                else:
                    lowercase_string += char
            return lowercase_string

        def remove_spaces(string):
            return string.replace(" ", "")

        def is_palindrome(a):
            length = len(a)
            for i in range(length // 2):
                if a[i] != a[length - 1 - i]:
                    return False
            return True

        string = input('Enter string: ')
        converted_string = convert_to_lowercase(string)
        checked = remove_spaces(converted_string)

        if is_palindrome(checked):
            print(string + ' is a palindrome')
        else:
            print(string + ' is not a palindrome')

    def four_1():
        def is_power_of(a, b):
            if a <= 0 or b <= 0:
                return False
    
            while a != 1:
                if a % b != 0:
                    return False
                a = a / b
            return True

        a = float(input('What is a?'))
        b = float(input('What is b?'))

        print(is_power_of(a, b))  

    def five_1():
        def find_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        num1 = float(input('input a. '))
        num2 = float(input('input b. '))

        gcd = find_gcd(num1, num2)
        print('the gcd of ', num1, ' and ', num2, 'is', gcd )

chapter6 = Chapter_6
#chapter6.two_1()
#chapter6.three_2()
#chapter6.four_1()
#chapter6.five_1()

class Chapter_7():
    def one_1():
        def mysqrt(x):
         return x ** 0.5

        def abs_diff(a,b):
            return abs(a - b)

        print("Number\t\tmysqrt\t\tmath.sqrt\tDifference")
        print('------------------------------------------------------')

        a = 1
        a_max = 10

        while a <= a_max:
            mysqrt_result = mysqrt(a)
            math_sqrt_result = math.sqrt(a)
            difference = abs_diff(mysqrt_result, math_sqrt_result)

            print(f"{a}\t\t{mysqrt_result:.4f}\t\t{math_sqrt_result:.4f}\t\t{difference:.4f}")
            a += 1

    def two_1():
        def eval_loop():
            while True:
                user_input = input('Enter an expression. or (exit) to exit >>')

                if user_input == "exit":
                    break

                try:
                    result = eval(user_input)
                    print('result:', result)
                except Exception as e:
                    print("error:", e)
                    
        eval_loop()

    def three_1():
        def formula():
            k = 0
            y = 0
            x = (2 * (math.sqrt(2))) / 9801
            while True:
        
                numerator = math.factorial(4 * k) * (1103 + (26390 * k))
                denominator = (math.factorial(k) ** 4) * (366 ** (4 * k))
        
                a = x * (numerator / denominator)
                y += numerator / denominator

                if abs(a) < 1e-15:
                    break
                k += 1
    
            return 1 / (x * y)

        print(formula())

chapter7 = Chapter_7
#chapter7.one_1()
#chapter7.two_1()
#chapter7.three_1()

class Chapter_8():

    def two_1():

        def count_letter(word, letter):
            count = 0
            for char in word:
                if char == letter:
                    count += 1
            return count

        word = "banana"
        letter = "a"
        count = count_letter(word, letter)
        print(count)

        count_letter(word, letter)
    
    def three_1():
        #im not sure if this is on a techicality or if its legaly on one line.
        a = str(input('Is it a palendrome? >>>')); print(a.lower() == a.lower()[::-1])

    def five_1():
        def cipher(text,shift):
            encrypted_text=""

            for char in text:
                if char.isalpha():
                    if char.isupper():
                        start = ord('A')
                    else:
                        start = ord('a')

                    encrypted_char = chr((ord(char) - start + shift) % 26 + start)
                    encrypted_text += encrypted_char
                else:
                    encrypted_text += encrypted_char

            return encrypted_text

        text = str(input('What do you want to encrypt >>> '))
        shift = int(input("give me a number >>> "))
        encrypted_text = cipher(text, shift)
        print(encrypted_text)

chapter8 = Chapter_8
#chapter8.two_1()
#chapter8.three_1()
#chapter8.five_1()

class Chapter_9():
    def one_1():
        def long_words(text_file):
            with open(text_file, 'r') as file:
                wordlist = file.read().split()

                for word in wordlist:
                    if len(word) > 20:
                        print(word)
        long_words(text_file)

    def two_1():
        def no_e(text_file):
            with open(text_file, 'r') as file:
                words = file.read().split()
                total_words = len(words)
                words_without_e = []

                for word in words:
                    if 'e' not in word:
                        words_without_e.append(word)

                percentage_without_e = (len(words_without_e) / total_words) * 100
                print("words without the letter 'e' : ")
                for word in words_without_e:
                    print(word)

                print(f"\nPercentage of words without 'e' : {percentage_without_e:.2f}%")
        no_e(text_file)

    def three_1():
        with open(text_file, 'r') as file:
            words = file.read().split()
        def avoids(text_file, letters):
            filtered_list = []
            for word in words:
                contains_letter = False
                for letter in letters:
                    if letter in word:
                        contains_letter = True
                        break
                if not contains_letter:
                    filtered_list.append(word)
            for word in filtered_list:
                print(word)

        letters = input('Enter letters to remove words: ')
        avoids(text_file, letters)
        
    def four_1():
        with open(text_file, 'r') as file:
            word_list = file.read().splitlines()
        
        def uses_only(text_file, letters):
            for word in word_list:
                contains_only = True
                for letter in word:
                    if letter not in letters:
                        contains_only = False
                        break
                if contains_only:
                    print(word)

        letters = input('Enter letters to filter words: '  )
        uses_only(text_file, letters)

    def five_1():
        with open(text_file, 'r') as file:
            words = file.read().split()
        def use_all(text_file, letters):
            filtered_list = []
            for word in words:
                contains_letter = True
                for letter in letters:
                    if letter not in word:
                        contains_letter = False
                        break
                if contains_letter:
                    filtered_list.append(word)
            for word in filtered_list:
                print(word)

        letters = input('Enter letters to add words: ')
        use_all(text_file, letters)

    def six_1():
        with open(text_file, 'r') as file:
            words = file.read().split()

        def is_abecedarian(word):
            previous = word[0]
            for c in word:
                if c < previous:
                    return False
                previous = c
            return True
        
        filtered_list = []
        for word in words:
            if is_abecedarian(word):
                filtered_list.append(word)
        
        for word in filtered_list:
            print(word)

    def seven_1():
        with open(text_file, 'r') as file:
            words = file.read().split()

        def triple_consecutive(words):
            for word in words:
                for i in range(len(word) - 5):
                    if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
                        print(word)
                        break
        triple_consecutive(words)

    def eight_1():
        def is_palindrome(num, a, b):
            num_str = str(num)[a:a + b]
            return num_str[::-1] == num_str
        
        def test(num):
            return(is_palindrome(num, 2, 4) and is_palindrome(num + 1, 1, 5) and is_palindrome(num + 2, 1, 4) and is_palindrome(num + 3, 0, 6))

        def test_all():
            num = 100000
            while num <= 999999:
                if test(num):
                    print(num)
                num = num + 1
        test_all()
        print()
        #even the code from the link isnt working idk what to do when i get better ill redo this one

    def nine_1():
        def age_is_palendrome():
            def age(num, length):
                return str(num).zfill(length)

            def check_palindrome(num, rev):
                return age(num, 2) == age(rev, 2)[::-1]

            def age_check(diff, flag=False):
                my_age = 0
                a = 0
                while True:
                    moms_age = my_age + diff
                    if check_palindrome(my_age, moms_age) or check_palindrome(my_age, moms_age + 1) or check_palindrome(my_age, moms_age - 1):
                        a += 1
                        if flag:
                            print(my_age, moms_age)
                    if moms_age > 100:
                        break
                    my_age += 1
                return a

            def age_diff():
                diff = 18 
                while diff < 40:
                    length = age_check(diff)
                    if length > 0:
                        print(diff, length)
                    diff += 1
    
            print()
            age_diff()
            age_check(18, True)
        age_is_palendrome()

chapter9 = Chapter_9
#chapter9.one_1()
#chapter9.two_1()
#chapter9.three_1()
#chapter9.four_1()
#chapter9.five_1()
#chapter9.six_1()
#chapter9.seven_1()
#chapter9.eight_1()
#chapter9.nine_1()

class Chapter_10():
    def one_1():
        #t = [1, 2, 3]
        t = [[1, 2], [3], [4, 5, 6]]
        def nested_sum(t):
            total = 0
            for x in t:
                if isinstance(x, list):
                    total += nested_sum(x)
                else:
                    total += x
            return total
        result = nested_sum(t)
        print(result)

    def two_1():
        t = [1, 2, 3]
        def cumsum(t):
            total = 0
            result = []
            for x in t:
                if isinstance(x, list):
                    total += nested_sum(x)
                    result.append(total)
                else:
                    total += x
                    result.append(total)
                
            return result
        result = cumsum(t)
        print(result)

    def three_1():
        t = [1, 2, 3, 4]
        def middle(t):
            length = len(t)
            if length % 2 == 0:
                a = length // 2 - 1
                a2 = length // 2
                c = [t[a], t[a2]]
            else:
                b = length // 2
                c = [t[c]]
            print(c)

        middle(t)
    
    def four_1():
        t = [1, 2, 3, 4]
        def chop(t):
            t.pop(0)
            t.pop(-1)
            return None

        chop(t)
        print(t)

    def five_1():
        #T = [1, 2, 3, 4]
        t = [2, 1, 3, 4]
        def is_sorted(t):
            a = sorted(t)
            if t == a:
                print('Is sorted')
            else:
                print('Is not sorted')
        is_sorted(t)

    def six_1():
        def is_anagram():
            a = str(input('Give me a word >>>'))
            b = str(input('Give me another word >>>'))
            if sorted(a) == sorted(b):
                print('Is an anagram')
            else:
                print('Is not an anagram')
        is_anagram()

    def seven_1():
        a = [1, 2, 2, 3, 4]
        #a = [1, 2, 3, 4, 5]
        def has_duplicates(a):
            if len(a) != len(set(a)):
                return True
                
            else:
                return False
        
        print(has_duplicates(a))
        
    def eight_1():
        
        def birthday_paradox(num_sims, num_people):
            duplicates = 0
            for i in range(num_sims):
                birthdays = set()
                for i in range(num_people):
                    birthday = random.randint(1, 365)
                    if birthday in birthdays:
                        duplicates += 1
                        break
                    birthdays.add(birthday)

            probability = 1 -  (duplicates / num_sims)
            return probability
        
        tests = 10000
        people = 23
        probability = birthday_paradox(tests, people)
        print(f'{people} {tests} {probability * 100}')
    
    def nine_1():
        def test(text_file):
            words = []
            with open(text_file, 'r') as file:
                for line in file:
                    word = line.strip()
                    words.append(word)
            return words

        result = test(text_file)
        print(result)

    def nine_2():
        def test(text_file):
            words = []        
            with open(text_file, 'r') as file:
                for line in file:
                    word = line.strip()
                    words = words + [word]
            return words
    
        result = test(text_file)
        print(result)
    
    def ten_1():
        with open(text_file, 'r') as file:
                words = file.read().split()
        def find_word(target_word, words):
            left = 0
            right = len(words) - 1

            while left <= right:
                mid = (left + right) // 2
                current_word = words[mid].strip()

                if current_word == target_word:
                    return mid
                elif current_word < target_word:
                    left = mid + 1
                else:
                    right = mid - 1

            return-1

        target = input('Give me a word. >>> ')
        
        result = find_word(target, words)
        if result == -1:
            print(target, 'not found')
        else:
            print(target, 'Found')

    def eleven_1():
    # this one does work it just takes 20 minutes  
        
        def reverse_pairs(words):
            reverse = []
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    word1 = words[i]
                    word2 = words[j]
                    if word1 == word2[::-1]:
                        reverse.append((word1, word2))
            return reverse

        with open(text_file, 'r') as file:
            words = file.read().split() 

        result = reverse_pairs(words)
        for pair in result:
            print(pair[0], pair[1])

    def twelve_1():
        #this one takes way too long
        with open(text_file, 'r') as file:
                words = file.read().split()
        def find_interlocking_pairs(words):
            interlocking_pairs = []

            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    combined_words = words[i] + words[j]
                
                    if combined_words in words:
                        pair = (words[i], words[j], combined_words)
                        interlocking_pairs.append(pair)

            return interlocking_pairs
        pairs = find_interlocking_pairs(words)    

        for pair in pairs:
            word1, word2, combined_words = pair
            print(f'{word1}, {word2}, {combined_words}')

chapter10 = Chapter_10
#chapter10.one_1()
#chapter10.two_1()
#chapter10.three_1()
#chapter10.four_1()
#chapter10.five_1()
#chapter10.six_1()
#chapter10.seven_1()
#chapter10.eight_1()
#chapter10.nine_1()
#chapter10.nine_2()
#chapter10.ten_1()
#chapter10.eleven_1()
#chapter10.twelve_1()

class Chapter_11():

    def one_1():
        def read_words(text_file):
            word_dict = {}

            with open(text_file, 'r') as file:
                for line in file:
                    words = line.split()
                    for word in words:
                        word_dict[word] = None
            return word_dict
    
        def check_word(word, word_dict):
            if word in word_dict:
                print("True")
            else:
                print('False')

        word_dict = read_words(text_file)
        input_word = input('Enter a word. >>> ')
        check_word(input_word, word_dict)
        read_words(text_file)

    def two_1():
        def invert_dict(dict_a):
            inveted_dict = {}
            for key, val in dict_a.items(): 
                inveted_dict.setdefault(val, []).append(key)
            return inveted_dict

        dict_a = {"a": 1, "b": 2, "c": 3, "z": 1,}
        inverted_dict = invert_dict(dict_a)
        for val, keys in inverted_dict.items():
            print(val, keys)
        
    def three_1():
        sys.setrecursionlimit(50000)
        memo = {}
        def ackermann_func(m, n):
            
            if (m, n) in memo:
                return memo[(m, n)]

            if m == 0:
                return n + 1
            elif m > 0 and n == 0:
                return ackermann_func(m - 1, 1)    
            elif m > 0 and n > 0:
                return ackermann_func(m - 1, ackermann_func(m, n - 1))

            memo[(m, n)] = result 
            return mysqrt_result

        num_1 = float(input('Enter first number. >>>'))
        num_2 = float(input('Enter second number. >>>'))

        print(ackermann_func(num_1, num_2))

    def four_1():
        a = [1, 2, 3, 4, 5, 4]
        def has_duplicates(a):
            dict_b = {}
            for i in a:
                if i in dict_b:
                    return True
                else:
                    dict_b[i] = 1
            return False

        print(has_duplicates(a))

    def five_1():
        def rotate_word(word):
            rotated_word = ""
            for char in word:
                if char.isalpha():
                    if char.isupper():
                        start = ord('A')
                    else:
                        start = ord('a')

                    rotated_char = chr((ord(char) - start + 1) % 26 + start)
                    rotated_word += rotated_char
                else:
                    rotated_word += char
            return rotated_word


        def find_rotate_pairs(file_path):
            rotate_pairs = []

            with open(file_path, 'r') as file:
                    words = set(file.read().split())
                    for word in words:
                        rotated_word = rotate_word(word)
                        if rotated_word != word and rotated_word in words:
                            rotate_pairs.append((word, rotated_word))

            return rotate_pairs


        file_path = 'words.txt'
        rotate_pairs = find_rotate_pairs(file_path)
        if len(rotate_pairs) == 0:
            print('No rotate pairs found.')
        else:
            for pair in rotate_pairs:
                print(pair[0], pair[1])

    def six_1():

        def find_homophone_pairs(word_list):
            homophone_pairs = []
            word_set = set(word_list)

            for word in word_list:
                if len(word) == 5:
                    removed_1 = word[1:]
                    removed_2 = word[0] + word[2:]
                    if removed_1 in word_set and removed_2 in word_set:
                        homophone_pairs.append(word)

            return homophone_pairs


        def remove_letter(word, index):
            return word[:index] + word[index + 1:]

        with open('words.txt', 'r') as file:
            word_list = file.read().lower().split()

        solution_pairs = find_homophone_pairs(word_list)

        if len(solution_pairs) > 0:
            print("Solution pairs:")
            for word in solution_pairs:
                print(word)
        else:
            print("No solution pairs found.")


chapter11 = Chapter_11
#chapter11.one_1()
#chapter11.two_1()
#chapter11.three_1()
#chapter11.four_1()
#chapter11.five_1()
#chapter11.six_1()

class Chapter_12():
    def one_1():
        pass

chapter12 = Chapter_12
chapter12.one_1()