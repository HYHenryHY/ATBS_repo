import random

messages=['It is certain',
          'It is decidedly so',
          'Yes definitely',
          'Reply hazy try again',
          'Ask again later',
          'Cencentrate and ask again',
          'My reply is no',
          'Outlook not so good',
          'Very doubtful']


while True:
    print('Please enter your question (or blank if you want to quit)')
    myQuestion=input()
    if myQuestion !='':
        print(messages[random.randint(0,len(messages)-1)])
    else:
        break
    

