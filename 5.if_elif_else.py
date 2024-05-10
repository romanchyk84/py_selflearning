colors = ['green', 'yellow', 'red']
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

print('\n', '*** This part of the code is finished ***'*2, '\n')

