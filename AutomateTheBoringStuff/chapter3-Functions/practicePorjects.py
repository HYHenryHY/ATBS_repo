#The Collatz Sequence
import time, sys
print('In order to experience the collatz sequence, type a positive integer')

try: #try and except function for KeyboardInterrupt
    
    #defining The Collatz function/ local scope
    def collatz(number):
        global myInteger
    
        if (number % 2) == 0:  #the % operator returns zero if a even number 
            print(number//2)
            return number//2
        else:
            print(3 * number + 1)
            return 3 * number + 1
    #The Collatz function returns

    while True: #putting the myInteger variable inside the while loop. If outside, the program will be infinite
        print('Enter number:')
        try:
            myInteger=int(input())
            while myInteger != 1:
                myInteger=collatz(myInteger)
                time.sleep(0.1) #Pause for 0.1 sec
        except ValueError:
            print('Please enter an integer.')
    
except KeyboardInterrupt:
    sys.exit()
