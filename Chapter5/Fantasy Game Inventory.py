def displayInventory(d):
    c=0
    for i,j in d.items():
        print(j,i)
        c+=j
    print('Total number of items:',c)
d=eval(input("enter dictionary"))
print("Inventory:")
displayInventory(d)

#{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
