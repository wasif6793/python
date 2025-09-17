#def statement is used to define functions in python, with the syntax:

#def <name> (<parameters>):
#    """documentation string"""
#    <code>


#Square function
def square(x):
    return x * 2
print("Using square func: ",square(3))
print()

#multiply
def multi(x,y):
    return x *y
print("Using multiply func: ",multi(2,4))
print()

#min and max value
def minmax(data):
    return min(data), max(data)
print("Finding min and max values: ",minmax([1,2,3,4,6,5,99,87,65]))
print()
