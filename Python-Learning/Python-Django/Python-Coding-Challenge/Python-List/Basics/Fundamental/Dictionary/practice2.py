""" 
    🍽️ 2. Menu System (Items & Prices)
"""


menu = {
    'Pizza': 120,
    'Burger': 150,
    'Cheese-Bread': 80,
    'Cold-drink': 50
}


print('--------------MENU--------------')

for item, value in menu.items():
    print(f"{item}: ${value}")

order = input('What would you like to order?')
if order in menu:
    print(f'{order} costs will be ${menu[order]}')
else:
    print('Menu items not available')