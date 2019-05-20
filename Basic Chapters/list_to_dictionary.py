def display_inventory(inventory):
    num = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        num += v
    print('Total: ' + str(num))


def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
display_inventory(inv)
