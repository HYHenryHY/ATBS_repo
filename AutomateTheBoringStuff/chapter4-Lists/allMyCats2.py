#How are lists good? Imagine putting assigning 6 cat names to 6 variables: catNameX
#for example:

#   print=('Enter the name of cat 1:')
#   catNameX=input()
#   ...
#   print'(The cat names are:')
#   print(catName 1 + '' +catName2 + '' + .... + '' + catNameN)

catNames=[]
while True:
    print('Enter the name of cat ' + str(len(catNames)+1)+
          ' (or enter nothing to stop.):')
    name=input()
    if name == '':
        break
    catNames=catNames + [name] #list concentration
print('The cat names are:')
for name in catNames:
    print(' '+ name)
