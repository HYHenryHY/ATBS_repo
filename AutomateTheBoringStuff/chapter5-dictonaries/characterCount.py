message='It was a bright cold day in April, and the clocks were striking \
thirteen.'
count={}

for x in message:
    count.setdefault(x,0) #1
    count[x]=count[x] +1 #2 can also be written as count[x] =+ 1

print(count)
