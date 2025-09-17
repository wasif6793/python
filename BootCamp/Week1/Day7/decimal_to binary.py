num = int(input("Enter decimal number: "))
binary = ""
n = num
while n > 0:
    r = n % 2
    binary = binary +  str(r)
    n = n // 2
rev = binary[::-1]
print(rev)
