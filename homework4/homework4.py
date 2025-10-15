fav_foods = ["sushi", "peaches", "steak", "cookies", "rice"]
print(fav_foods[1])
print(fav_foods[-1])

fav_foods.append("lychee")
print(fav_foods)

fav_foods.insert(0,"apple")
print(fav_foods)

fav_foods.remove("steak")
print(fav_foods)

print(len(fav_foods))

print(str(fav_foods).upper())

print(fav_foods[0:6:5])

def is_there_potato(fav_foods):
    if "potato" in fav_foods:
        print("A potato!")
    else:
        print("No potato!")
is_there_potato(fav_foods)


numbers = range(0,20)
def get_first_15(numbers):
    return list(numbers[0:15])
print(get_first_15(numbers))
step1 = list(get_first_15(numbers))

def get_every_5th(step1):
    return step1[0:15:4]
print(get_every_5th(step1))
step2 = get_every_5th(step1)

def reverse_and_stride(step2):
    reverse_fifth = step2[::-1]
    return reverse_fifth[0::2]
print(reverse_and_stride(step2))
step3 = reverse_and_stride(step2)


list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])

def sum_nested(numbers):
    total = 0
    for sublist in numbers:
        total += sum(sublist[:3])
    return total
print(sum_nested(numbers))


def one_to_twenty_five():
    twenty_five = []
    for x in range(0, 25, 5):
        row = []
        for y in range(x + 1, x + 6):
            row.append(y)
        twenty_five.append(row)
    return twenty_five
print(one_to_twenty_five())

twenty_five = one_to_twenty_five()
def no_three_multiples(twenty_five):
    for sublist in twenty_five:
        for i, value in enumerate(sublist):
            if value%3 == 0:
                sublist[i] = "?"
    return twenty_five
    i+=1
mult_three = no_three_multiples(twenty_five)
print(mult_three)

def not_equal_to(mult_three):
    total = 0
    for sublist in mult_three:
        filtered = [x for x in sublist if x != '?']
        total += sum(filtered[:4])
    return total

add_no_questions = not_equal_to(mult_three)
print(add_no_questions)


ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for (key) in ages:
    print(key, ages[key])


twenty_five = one_to_twenty_five()
def no_three_multiples(twenty_five):
    for sublist in twenty_five:
        for i, value in enumerate(sublist):
            if value%3 == 0:
                sublist[i] = "?"
    return twenty_five
    i+=1
mult_three = no_three_multiples(twenty_five)
print(mult_three)

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"},
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,   
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"}
    }

targets.update({"Pollux": {
    "RA": "07h 45m 18.9s",
    "Dec": "+28° 01′ 34″",
    "Magnitude": 1.14,
    "Spectral Type": "KOIII"}})


for key in targets:
        print(key)
    
for name, data in targets.items():
    print(f"{name}, {data['Spectral Type']}")

for target in targets:  
    if targets[target]["Magnitude"] > 0.1:
        print(target)

targets.update({"Pollux": {
    "RA": "07h 45m 18.9s",
    "Dec": "+28° 01′ 34″",
    "Magnitude": 1.14,   
    "Spectral Type": "KOIII"}})
    
def split_data(dec_str):
    dec_str = dec_str.replace('−', '-')
    dec_str = dec_str.lstrip('+')
    deg_part = dec_str.split('°')[0]
    return int(deg_part)   

def find_closest_to_20_deg(targets):
    closest_target = None
    min_diff = float('inf')
    for name, data in targets.items():
        dec_str = data['Dec']
        dec_deg = split_data(dec_str)
        diff = abs(dec_deg - 20) 
        if diff < min_diff:
            min_diff = diff
            closest_target = name
    if closest_target:
        print(f"{closest_target}")
find_closest_to_20_deg(targets)
    
print("Orion!")
