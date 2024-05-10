"""colors = ['green', 'yellow', 'red']
color = 'green'
if color in colors:
    print(f"{color}, this color is in the list. You won 10 points.")

colors_1 = ['green', 'yellow', 'red']
color1 = 'blue'
if color1 in colors_1:
    print(f"{color1}, this color is in the list. You won 10 points.")
else:
    print(f"{color1}, it is not in the list.")

print('\n', '*** The end of this part ***'*2, '\n')

alien_color = ['green', 'yellow', 'red']
color = input("Choose your color (for example, green): ")
if color.lower() in alien_color:
    if color == 'green':
        print('You won 5 points!')
    # print("Игрок заработал 5 очков")
if color.lower() in alien_color:
    if color == 'yellow' or color == 'red':
        print("You won 10 points!")
# if color.lower() not in alien_color:
else:
    print("Sorry, this color is absent ")

print('\n', '*** This part of the code is finished ***'*2, '\n')

tsveta = ['green', 'yellow', 'red']
tsvet = 'yellow'
if tsvet in tsveta:
    if tsvet == 'green':
        print(f'{tsvet} player won 5 points!')
    elif tsvet == 'yellow':
        print(f'{tsvet}, a player won 10 points!')
    elif tsvet in tsveta:
        print(f'{tsvet}, a player won 15 points...')
else:
    print(f'{tsvet}, this color is not in the list')

print('\n', '*** This part of the code is finished ***'*2, '\n')"""

age = int(input("Input age (for example, 2):"))
if age >= 0 and age < 2:
    print("It's an Infant")
elif age >= 2 and age < 4:
    print("It's a Toddler")
elif age >= 4 and age < 13:
    print("It's a Kid or Baby")
elif age >= 13 and age < 20:
    print("It's a Teenager")
elif age >= 20 and age < 25:
    print("It's a Young adult age")
elif age >= 25 and age < 55:
    print("it's an Adult age")
elif age >= 55 and age < 65:
    print("It's a Senior-citizen age")
elif age in range(65, 131):
    print("It's an Elderly age!")
elif age < 0:
    print("Age can't be negative")

print('\n', '*** This part of the code is finished ***'*2, '\n')

ages = {"infant": (0, 2),
        "toddler": (2, 4),
        "child": (4, 13),
        "teenager": (13, 20),
        "young adult": (20, 25),
        "adult": (25, 55),
        "senior-citizen age": (55, 65),
        "elderly": (65, 150)
        }
years = int(input("Enter your age: "))
for age, (down, up) in ages.items():
    if down <= years < up:
        print(f"Ваш возраст соответствует категории: {age.title()}")

print('\n', '*** This part of the code is finished ***'*2, '\n')