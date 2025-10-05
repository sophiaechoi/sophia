def say_goodbye(name):
    print("Goodbye,", name)
name = "sophia"
print(say_goodbye(name))
result = say_goodbye(name)

def circle_area(r):
    return 3.14*r**2
print(circle_area(5))
r = 5
result = circle_area(r)

def subtract(a,b):
    return a-b
print(subtract(5,4))
def multiply(a,b):
    return a*b
print(multiply(5,4))
def divide(a,b):
    return a/b
print(divide(5,4))


todays_temperatures = [72,75,73,71,68,67]
def what_to_wear(todays_temperatures):
    return (min(todays_temperatures), max(todays_temperatures))
print(what_to_wear(todays_temperatures))

Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7

def is_weekend(day):
    if 5<day<=7:
        return True
    else:
        return False
print(is_weekend(Monday))
#returns False

def fuel_efficiency(distance,fuel):
    return distance/fuel
print(fuel_efficiency(14,7))



def new_pow(x,y):
    result = 1
    is_negative = y<0
    y = abs(y)
    for i in range(0,y):
        result*=x
    if is_negative:
     return 1 / result
    else:
     return result
print(new_pow(2,4))

list = [2,4,1,5,6,2,8]
def minimum(list):
    base = list[0]
    for i in list:
        if i<base:
            base = i
    return base
print(minimum(list))

def maximum(list):
    base = list[0]
    for i in list:
        if i>base:
            base = i
    return base
print(maximum(list))

def minimum2(list):
    i = 1
    base = list[0]
    while i < len(list):
        if list[i] < base:
            base = list[i]
        i += 1
    return base
print(minimum2(list))

def maximum2(list):
    i = 1
    base = list[0]
    while i < len(list):
        if list[i]>base:
            base = list[i]
        i+=1
    return base
print(maximum2(list))

def sum_of_digits(x):
    digits = str(x)
    total = 0
    for i in digits:
        total+=int(i)
    return total
print(sum_of_digits(2468))

def encrypt(x):
    return x%10*10**(len(str(abs(x)))-1) + x//10

x = 524291
result = encrypt(x) #the last digit is moved to the front fo the number
print(f"The result of Secret Code (5.4) with x = {x} is {result}.")