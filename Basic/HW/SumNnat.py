#Program to sum n natural numbers

def sum(num):
    return (num *(num + 1)) /2

n = int(input("Enter value of n: "))
print(f"Sum of {n} natural number is {sum(n)}")