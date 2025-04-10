"""
    Create a dictionary for a contact book (name → phone number).

    Make a menu system with items and prices.

    Count word frequency in a string using a dict.
"""

#Contact Book (Dictionary Practice)

contacts = {
        'Harry': 8849964295,
        'Kapil': 9978742881,
        'Papa': 9879316047
}

# Add new contact
name = input('Enter the name: ')
phone = input('Enter the phone number: ')
contacts[name] = phone

# Search for contact
search = input('Enter the number you looking for?')
print(f"{search}'s number is {contacts.get(search, 'not found')}")
