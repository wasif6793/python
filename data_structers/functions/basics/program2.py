def findLargest(a,b,c):
    if(a> b and a>c):
        big = a
    elif(b> a and b>c):
        big = b
    else:
        big = c
    return big
x = int(input("Enter first value: "))
y = int(input("Enter second value: "))
z = int(input("Enter the third value: "))
res = findLargest(x,y,z)
print("Max value is:", res)