inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ""
print(inventory)
inventory["pocket"] = 'seashell', 'strange berry', 'lint'
print(inventory)
inventory["backpack"].remove(inventory["backpack"][1])
print(inventory)
inventory['gold'] += 50
print(inventory)
