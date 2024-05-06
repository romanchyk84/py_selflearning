# List - тип данных, когда в переменной нужно сохранить неограниченное число информации
import copy
"""
# list of names
names = ['Roman', 'Ilona', 'Aleksandr']
print(names[1])
print(names[2])
print(names[0])


message = f"I wish you a Merry Christmas"
# Обращение к элементу в списке по индексу. Индексация начинается с 0, а не с 1
print(f"{message} {names[0]}!")
print(f"{message} {names[1]}!")
print(f"{message} {names[2]}!")

vehicles = ['KIA', 'hyundai', 'honda', 'renault']
mes = "I'd like my next car to be"
# К элементам списка применимы методы, которые используются со строками (title(), upper(), lower())
print(f"{mes} {vehicles[2].title()} or {vehicles[3].upper()}")
"""
"""
motorcycles = ['honda', 'suzuki', 'yamaha']
print(motorcycles)

motorcycles.append('dukati')
print(motorcycles)
print(len(motorcycles))

motorcycles.insert(1, 'java')
print(motorcycles)

# Постоянная сортировка
sort_list = copy.deepcopy(motorcycles)
sort_list.sort()
print(sort_list)
sort_list.sort(reverse=True)
print(f'Обратно Отсортированный список: {sort_list}')

# Временная сортировка sorted(iterable) / Временная обратная сортировка sorted(iterable, reverse=True)
print(motorcycles)

print(f'Vremennaya sortirovka viglyadit tak:', sorted(motorcycles))
print(f'Bez sortirovki:', motorcycles)
print(f'Vremennaya obratnaya sortirovka:', sorted(motorcycles, reverse=True))

"""
# For cycle
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'I can\'t wait to see you next time, {magician.title()}!\n')

while len(magicians) != 0:
    popped_list = [magicians.pop()]

    print(popped_list)
print("Thank you, everyone. That was a great magic show!\n")

pizzas = ['Carbonara', 'Diablo', 'Barbequ', 'Margarita']
end_message = f'I really love pizza!'
for pizza in pizzas:
    print(f'I like {pizza.lower()} pizza.')
print(f'{end_message}\n')

animals = ['cat', 'tiger', 'cougar']
for an in animals:
    print(f"A {an} belongs to the cat family.")
print('Any of these animals love meat')
