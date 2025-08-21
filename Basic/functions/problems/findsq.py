
val = int(input("Enter a number: "))

def sq(val):
    return val ** 2

print(f"Square of {val} is ",sq(val))

def cube(val):
    return val *sq(val)

print(f"Cube of {val} is ",cube(val))