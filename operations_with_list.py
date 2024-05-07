for value in range(5):
    print(value)
    
print("-"*47)

numbers = []
for n in range(1, 11):
    kv = n**2
    numbers.append(kv)
print(numbers)    

print("-"*47)

chisla = list()
for chislo in range(1,11):
    chisla.append(chislo**2)
print(chisla)


x = []
for y in range(2,21,2):
    x.append(y**2)
print(x)  
print(min(x))
print(max(x))
print(sum(x))
print(sum(chisla))
print("-"*47)

kvadraty = [value**4 for value in range(0,11)]
print(kvadraty)
print(sum(kvadraty))
print("-"*47)

# используя цикл for вывести числа от 1 до 20 включительно
for k in range(1,21):
    print(k)
    
print("-"*47)

"""
spisok = [value for value in range(1,1000001)]
print(spisok)
print(min(spisok))
print(max(spisok))
print(sum(spisok))
"""

list = []
for k in range(1,20,2):
    list.append(k)
print(list) 

list1 = [q for q in range(1,20,2)]
print(list1)

print("-"*47)
# Создание списка чисел от 3 до 30, кратного 3
spis = [value for value in range(3,31,3)]
print(spis)
# Создание списка, кратного 3. второй способ.
spiski = []
for values in range(3,40):
    if values%3 == 0:
        spiski.append(values)
print(spiski)
print("-"*47)

# Создание списка от 1 до 10, возведённого в куб
kubs = []
for values in range(1,11):
    value = values**3
    kubs.append(value)
print(kubs)

print("-"*47)

# Генератор кубов. Создание списка от 1 до 10 и возведение в куб
kub_gen = [value**3 for value in range(1,11)]
print(kub_gen)

# Работа с частью списка с помощью задания первого и последнего индекса элемента, с которым будем работать
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'david', 'jason']
# Выводит элемента списка под индексами 0, 1 и 2
print(players[0:3])
# Выводит элементы под индексами 0, 1, 2 и 3. До 4 элемента, 4 не выводит
print(players[:4])
# Выводит 3 элемента списка, начиная с самого последнего
print(players[-3:])
print(players)
print(players[0:7:5])

# Перебор содержимого сегмента
for player in players[0:4]:
    print(player.title())

# Копирование списков
my_meal = ['pizza', 'pelmeni', 'plov', 'borsch', 'apple cake']
print(f"My favorite meal are:", my_meal)
# Copy my list of meal to friend's list
friend_meal = my_meal[:]
print(f"My friend's favorite meal:", friend_meal)

print(id(my_meal))
print(id(friend_meal))

my_meal.append('meatballs')
friend_meal.append('shawarma')
print(f"My new meal list is:", my_meal)
print(f"Friend's new meal list is:", friend_meal)
print(f'*** the end ----- the end ----- the end ***\n')

new_list = ['roman', 'ilona', 'alexander', 'maks', 'olya', 'masha', 'alyona', 'oleg', 'natasha']
print('The first three elements in the list are:')
for name in new_list[0:3]:
    print(name.title())
print(f'\nThree elements from the middle of the list are:')
for name in new_list[3:6]:
    print(name.upper())
print(f'\nAnd the last three elements in the list are:')
for name in new_list[-3:]:
    print(name.title())


