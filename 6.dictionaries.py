
# Словари и операции с ними
# Словарь, содержащий разнообразную информацию об одном объекте
alien_0 = {'color': 'green', 'points': 5, 'key': 'value'}
print(alien_0['color'])     # Вывводим значение по ключу color
print(alien_0['points'])    # Выводим значение по ключу points

new_points = alien_0['points']
print(f"Your just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print('*'*50)

alien_1 = {}    # Создание пустого словаря
alien_1['color'] = 'red'    # Добавление первой пары "ключ": "значение"
alien_1['points'] = 10      # Добавление второй пары "ключ": "значение"
print(f"Alien color is {alien_1['color']}")     # Вывод текущего цвета

alien_1['color'] = 'yellow'     # Изменение первой пары, меняем значение цвета с green на yellow
print(f"New alien color is {alien_1['color']}")

print('*'*50)

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
print(f"New position: {alien_2['x_position']}")

print('*'*50)

print(alien_2)
alien_2['points'] = 5
print(alien_2)
del alien_2['points']   # Удаление ненужной пары "ключ: значение" из словаря. Удаление без возможности восстановления
print(alien_2)
x = alien_2.pop('speed')    # Удаление с возможностью восстановления, запись в переменную
print(f'Мы удалили ключ "speed", которому соответствует значение "{x}"')
print(f'New dictionary looks like: {alien_2}')

print('*'*50)

# Словарь, содержащий однообразную информацию о многих объектах
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}")
lang = favorite_languages['sarah'].title()
print(f"'{lang}' is Sarah's favorite language.")
