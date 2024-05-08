"""
Tuples  - Кортежи, это списки, которые нельзя изменять в процессе работы программы обычными методамо,
но можно внести изменения, изменив саму переменную
"""
# tuples
dimensions = [200, 75, 50]
print(dimensions)
# print(f"Размеры комнаты 'Длина', 'Ширина' и 'Высота':")
# for dimension in dimensions:
#     print(dimension)
# dimensions = (320, 100, 75)
# print(f"\nThe new dimensions of a room are (Length, Width and Height):")
# for dimension in dimensions:
#     print(dimension)

print(type(dimensions), dimensions)

# Methods append() and pop() are not available for tuples
# dimensions.append(555)
# dimensions.pop(555)

# del  - команда может удалить кортеж целиком, но не отдельный элемент кортежа (как например в списке)
# del dimensions[index]  - удаление элемента по индексу (работает со списком, но не с кортежем!)
del dimensions
print(dimensions)
