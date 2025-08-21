import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

res = math.gcd(a, b)

print(res)

# USING FUNCTION

def gcd(a, b):
    while(a != b):
        if(a > b):
            a = a - b
        else:
            b = b - a
    return b

print("GCD using function",gcd(a, b))