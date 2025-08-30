#Local scope

def greet():
    msg = "Hii local"
    print(msg)
greet()
#print(msg)

#global scope

greeting = "Hi global"

def say_hii():
    print(greeting)

say_hii()
print(greeting)