def spam():
    eggs='spam local' #1
    print(eggs) #prints 'spam local'

def bacon():
    eggs='bacon local' #2
    print(eggs) #prints 'bacon local'
    spam()
    print(eggs) #prints 'bacon local'

eggs='global'
bacon()
print(eggs) #prints 'global'
