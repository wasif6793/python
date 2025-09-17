#Lambda fn is an anonymous, single-expression functions defined using the lambda keyword
from functools import reduce
#Syntax
#lambda arguments: expression

add = lambda x,y: x +y
print(add(3,5))

#map() , filter() and iterable()

#map()   It  applies filter a function to each item in an iterable
numbers = [1,2,3,4]
squares = map(lambda x: x**2,numbers)
print(list(squares))

#filter()  It filters items based on a condition
evenList  =  filter(lambda x:x % 2 == 0,numbers)
print(list(evenList))

#reduce()  It reduces an iterable to a single value
product = reduce(lambda x,y:x * y,numbers)
print(product)

