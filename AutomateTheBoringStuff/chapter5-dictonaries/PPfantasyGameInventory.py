#Fantasy Game Inventory

#Structure of the player´s inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total=item_total+v
    print("Total number of items: " + str(item_total))


### List to Dictonary Function for Fantasy Game Inventory ###

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item]=inventory[item]+1
    return inventory

inv = {'gold coin': 42, 'rope': 1} #new inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv=addToInventory(inv, dragonLoot)
displayInventory(inv)
