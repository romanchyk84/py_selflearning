"""
Tuples  - Кортежи, это списки, которые нельзя изменять в процессе работы программы обычными методамо,
но можно внести изменения, изменив саму переменную
"""
# tuples
dimensions = (200, 75, 50)
print(f"Размеры комнаты 'Длина', 'Ширина' и 'Высота':")
for dimension in dimensions:
    print(dimension)
dimensions = (320, 100, 75)
print(f"\nThe new dimensions of a room are (Length, Width and Height):")
for dimension in dimensions:
    print(dimension)

