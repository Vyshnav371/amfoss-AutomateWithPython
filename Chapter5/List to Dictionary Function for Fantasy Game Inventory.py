def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] not in inventory.keys():
            inventory[addedItems[i]]=1
        else:
            inventory[addedItems[i]]+=1
    return(inventory)
def displayInventory(d):
    c=0
    print("Inventory:")
    for i,j in d.items():
        print(j,i)
        c+=j
    print('Total number of items:',c)
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
