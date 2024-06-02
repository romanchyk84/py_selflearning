users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for user_name, user_info in users.items():
    print(f'Username : {user_name}')
    full_name = f"{user_info['first'].title()} {user_info['last'].title()} "
    location = f"{user_info['location']}"
    print(f'\t{full_name.title()}')
    print(f'\t{location.title()}')

