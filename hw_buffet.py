buffet = ('ukrainian borsch', 'russian schi', 'belarus draniky', 'olivie', 'meatballs')
print(f'\nYou can taste five dishes from different cuisines in our restaurant: ')
for dish in buffet:
    print('\t',dish.title())
print(id(buffet))

# buffet.append('uzbekskiy plov')
# buffet.pop('olivie')

print("\nSome dishes have been changed on our menu, so can see our new menu:")
buffet = ('ukrainian borsch', 'russian schi', 'belarus draniky', 'uzbekskiy plov', 'moldavian mamalyga')
for dish in buffet:
    print('\t', dish.title())
print(id(buffet))
