allGuests={'Alice':{'apples':5,'pretzels':12},
           'Bob':{'ham sandwhices':3,'apples':2},
           'Carol':{'cups':3,'apple pies':1}}

def totalBrought(guest, item):
    numBrought=0
    for k, v in guest.items(): #1
        numBrought=numBrought+v.get(item,0) #2
    return numBrought

print('Number of things being brought:')
print('- Apples         ' +str(totalBrought(allGuests,'apples')))
print('- Cups           ' + str(totalBrought(allGuests, 'cups')))
print('- Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print('- Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print('- Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))