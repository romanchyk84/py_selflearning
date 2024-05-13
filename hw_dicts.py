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
