#9 Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

while True:
    print('Please enter a integer value')
    spam=input()

    if spam=='q':
        break
    elif spam=='1':
        print('Hello')
    elif spam=='2':
        print('Howdy')
    else:
        print('Greetings')

print('Thank you')
    
#13 Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

#using the for loop
for i in range (1,11,1):
    print(i)

#using the while loop
i=1
while i<11:
    print(i)
    i=i+1
