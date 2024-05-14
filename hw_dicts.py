man = {'first_name': 'jason',
       'last_name': 'statham',
       'age': 56,
       'city': 'london',
       }
print(f"His name is {man['first_name'].title()}")
print(f"{man['first_name'].title()}'s last name is {man['last_name'].title()}")
print(f"{man['first_name'].title()} {man['last_name'].title()} is {man['age']} y.o.")
print(f"He lives in the city of {man['city'].title()}")

print('\n', '-' * 15, 'The end', '-' * 15, '\n')

fav_numbers = {
    'roman': 5,
    'ilona': 10,
    'sasha': 15,
    'maksim': 20,
    'olya': 25,
    }
print(f"Roman's favorite number is {fav_numbers['roman']}")
print(f"{fav_numbers['ilona']} is Ilona's favorite number")
print(f"Sasha's favorite number is {fav_numbers['sasha']}")
print(f"{fav_numbers['maksim']} is Maksim's favorite number")
print(f"Olya's favorite number is {fav_numbers['olya']}")

print(f'\n', '*' * 5, 'Previous task using cycle for', '*' * 5, '\n')
for key in fav_numbers:
    print(f"{key.title()}'s favorite number is {fav_numbers[key]}")

# Создание Глоссария, словарь с типами данных и их значениями
glossary = {'string': 'data type that represents strings',
            'int': 'integer data type, whole numbers',
            'float': 'data type that represents numbers with a decimal points',
            'list': 'data type, represent collections of items, different types and can modify the elements in a list',
            'tuple': 'data type, represents collections of items, different types. But it can\'t be modified!',
            'dict': 'data type that represents collections of a "key-value" pairs',
            }
# Способ с двумя переменными (key) и (value)
for key, value in glossary.items():
    print(f'\n Data type: {key}')
    print(f' Meaning: {value}')
# Способ с использованием одной переменной (k)
# for k in glossary:
#     print(f'\nТип данных: {k} \nЗначение: {glossary[k]}')

for d_type in glossary.keys():  # Перебор всех ключей в словаре Глоссарий
    print(f'{d_type.upper()}')
