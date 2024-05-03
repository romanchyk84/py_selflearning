# Строки можно писать и в одинарных кавычках ''
name = 'Roman'
print(name)

# Строки можно писать и в двойных кавычках ""
name1 = "Kventin"
print(name1)

first_name = 'roman'
last_name = 'motorin'
print(first_name, last_name)

# f-string  f-строки, форматирование вывода, форматирование строки
first_name = 'kventin'
last_name = 'tarantino'
full_name = f'{first_name} {last_name}'
print(full_name)

nome = 'vasya'
prenome = 'pupkin'
print(f'{nome} {prenome}')

# title() Первый символ каждого слова делает заглавными,
# lower() Все символы преобразует в нижний регистр (сделает маленькими буквы),
# upper() весь текст будет преобразован в верхний регистр (большие буквы)
first_name = 'roman'
last_name = 'motorin'
print(first_name.title(), last_name.title())


first_name = 'roman'
last_name = 'motorin'
print(f'{first_name.upper()} {last_name.upper()}')

first_name = 'RoMAN'
last_name = 'MOtoRiN'
print(first_name.lower(), last_name.lower())

# Вывод с новой строки и табуляция при использовании f-строк
# \n  Вывод с новой строки,
# \t  отступ с табуляцией (4 пробела)
lang1 = 'Python'
lang2 = 'C++'
lang3 = 'JavaScript'
lang4 = 'PHP'
print(f'\n{lang4}\n\t{lang2}\n{lang1}\n\t{lang3}')

# 'что-либо'*n  Вывод чего-либо N-ое количество раз  (например '=='*30)
print(f'{lang1}','\n', '-'*30)

# Удаление лишних пробелов после слова, между словами
# strip()  Удаляет пробелы с обоих концов строки (слева и справа)
# lstrip() Удаляет отступы у левого края строки
# rstrip() Удаляет отступы у правого края строки
language = '  python '  # 2 отступа с левого края строки и 1 отступ в конце строки
print({language.rstrip()})
print({language.lstrip()})
print({language.strip()})

# Использование апострофа (') с двойнми и одинарными кавычнами
var = "One of Python's strengths is its diverse community"
print(var)
# При использовании апострофа (') с одинарными кавычками апостроф необходимо заэкранировать (\')
var = 'One of Python\'s strengths is its diverse community'
print(var)
