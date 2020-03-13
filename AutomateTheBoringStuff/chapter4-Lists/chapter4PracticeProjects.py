#Comma Code
#Output should be: 'apples, bananas, tofu, and cats'

import copy

def comma(someArgument):
    copyArgument=copy.copy(someArgument)
    if len(copyArgument) <2:
        print(copyArgument)
    else:
        copyArgument.insert(-1,'and')
        for index, item in enumerate(copyArgument): #instead of range(len(copeArgument))
            if len(copyArgument) == 2:
                print(copyArgument[index] + ' ',end='')
            else:   
                if index == len(copyArgument)-2:
                    print (copyArgument[index] + ' ', end='')
                elif index == len(copyArgument)-1:
                    print(copyArgument[index], end='')
                else:
                    print(copyArgument[index] + ', ', end='')
        
spam = ['apples','bananas','tofu','cats']
cake = ['eggs','flour','milk']
rice = ['seeds', 'water']
beef = ['meat']
cheese = []

comma(spam)

