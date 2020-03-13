birthdays={'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'} #1

while True:
    print('Enter a name: (blank to quit)')
    name=input()
    if name == '':
        break

    if name in birthdays: #2
        print(birthdays[name]+' is the birthday of ' + name) #3
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday=input()
        birthdays[name]=bday #4
        print('Birthday database udated')

        
