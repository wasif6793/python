num = int(input("Enter number: "))
val = 1
num2 = num
while num > 1:
    val *= num
    num -=1
print(f"Factorial of {num2} is {val}")