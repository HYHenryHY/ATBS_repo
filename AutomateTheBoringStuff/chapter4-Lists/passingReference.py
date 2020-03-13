def eggs(someParameter):
    someParameter.append('Hello')

spam=[1,2,3]
eggs(spam)
print(spam)


# mutable datatypes can be modified in place
# when assigning a MUTABLE datatypes like lists to a variable,
# you actually store a reference to the list and can be modified in place, while

# assigning immutable datatypes (tuples (immutable list) or string)
# you actually store the the evaluated value.
#A variable with immutable data (tuples or strings) can be overwritten with new immutable

