def evenorodd(a):
    if a % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"

num = int(input("Enter num to check for even or odd: "))
print(evenorodd(num))