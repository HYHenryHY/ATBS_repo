import random #1 imports the random module

def getAnswer(answerNumber): #2 the "getAnswer" function is defined, so execution skips
    if answerNumber== 1: #3
        return 'It is certain'
    elif answerNumber== 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

#4 r=random.randint(1,9) :the random.randint() function is called with two arguments (1,9)
#5 fortune=getAnswer(r) :the getAnswer() funciton is called with (r) as argument
#6 print(fortune) :the returned string is assigned to variable named "fortune" which is passed via the print() call

#since it is able to return values as arguments to another function call, we shorten to    
print(getAnswer(random.randint(1,9)))
