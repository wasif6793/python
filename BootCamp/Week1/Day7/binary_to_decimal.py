binary = int(input("Enter binary number: "))

decimal = 0
i = 0
while binary > 0:
    r = binary % 10
    decimal = decimal + r*(2**i)
    binary = binary // 10
    i+= 1

print(decimal)

