inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
#Add a key to inventory called 'pocket'  
#set the value of 'pocket' to be a list consisting of the strings'seashell', 'strange berry', and 'lint'.
inventory['pocket']=['seashell', 'strange berry', 'lint']

#remove('dagger') from the list of items stored under the 'backpack' key.
del inventory['backpack'][1]

# Add 50 to the number stored under the 'gold' key.
inventory['gold']=inventory['gold']+50

print(inventory)