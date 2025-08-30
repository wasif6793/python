def factorial(n):
    if n == 1 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter number for factorial: "))
print(f"Factorial is {factorial(num)}")
