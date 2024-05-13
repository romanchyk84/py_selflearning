
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

