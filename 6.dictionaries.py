
# Словари и операции с ними
alien_0 = {'color': 'green', 'points': 5, 'key': 'value'}
print(alien_0['color'])     # Вывводим значение по ключу color
print(alien_0['points'])    # Выводим значение по ключу points

new_points = alien_0['points']
print(f"Your just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

# del alien_0

alien_1 = {}    # Создание пустого словаря
alien_1['color'] = 'red'    # Добавление первой пары "ключ": "значение"
alien_1['points'] = 10      # Добавление второй пары "ключ": "значение"
print(f"Alien color is {alien_1['color']}")     # Вывод текущего цвета

alien_1['color'] = 'yellow'     # Изменение первой пары, меняем значение цвета с green на yellow
print(f"New alien color is {alien_1['color']}")

# Пришелец перемещается вправо.
# Вычисляем величину смещения на основании текущей скорости.
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_2['x_position']}")
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро
    x_increment = 3
alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"Новая позиция: {alien_2['x_position']}")
