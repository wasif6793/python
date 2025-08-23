def factorial(n):
    f =1
    for i in range(1, n+ 1):
        f = f * i
    return f

num = int(input("Enter num for factorial: "))
print("Factorial of",num,"is",factorial(num))

def rfact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * rfact(n-1)
print("Factorial of",num," using recursion is",rfact(num))