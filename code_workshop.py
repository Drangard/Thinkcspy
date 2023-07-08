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
