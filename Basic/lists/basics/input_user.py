ls =[]
n = int(input("Enter number of digits to enter in list: "))
for i in range (n):
    num = int(input("Enter a number: "))
    ls.append(num)

for i in ls:
    v = sum(ls)

print(v/n)