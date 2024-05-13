# Names in the list
names = ['roman', 'maksim', 'aleksey', 'admin', 'nikolay', 'ruslan']
for name in names:
    if name != 'admin':
        print(f"Hello,{name.title()}, thank you loging in again!")
    else:
        print(f"{name}, hello, would you like to see a status report?")

print('\n', '*'*50, '\n')

# Проверка списка, используя команду if, не пустой ли список. Если список пуст - вывести сообщение
list = ['roman', 'maksim', 'aleksey', 'nikolay', 'ruslan']
if len(list) > 0:
    for name in list:
        print(f"{name.title()}, have a nice day!")
else:
    print(f"This list is empty!")
"""
 Проверим, если список не пуст, будем удалять по одному элементу, пока не будет пуст. Удаленные элементы
 запишем в новый список.
"""
deleted_list = []
while len(list) != 0:
    x = list.pop()
    deleted_list.append(x.upper())
print(deleted_list)

print('\n', '*'*50, '\n')

current_users = ['rOMAn', 'ILONA', 'aleksandr', 'maksim', 'masha', 'olya']
new_users = ['oleg', 'kirill', 'aleksey', 'Roman', 'Ilona']
# Приведем первый список к нижнему регистру
current_users_lower = [name.lower() for name in current_users]
# print(current_users_lower, '\n\t', current_users)
# Сравним списки, чтобы узнать какие имена можно использовать, а какие уже заняты
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user.lower()}, this nickname is already used")
    else:
        print(f"{new_user.lower()}, this nickname is available.")

print('\n', '*'*50, '\n')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

