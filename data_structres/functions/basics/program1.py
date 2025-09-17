def finSquare(x):
    y = x * x
    return y

def findCube(x):
    z = x* x * x
    # we can also use like z = x * findSquare(x)
    return z

num  = int (input("Enter any num: "))
res = finSquare(num)
print("Square of given number: ", res)
res = findCube(num)
print("Cube of  a number: ",res)
