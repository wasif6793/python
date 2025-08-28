#Maximum of numbers
a = int(input("Enter A: "))

b = int(input("Enter B: "))

c = int(input("Enter C: "))

if( a > b and a >c):
    print(f"Maximum number is: a = {a}")
elif(b > c):
    print(f"Maximum number is: b = {b}")

else:
    print(f"Maximum number is: c = {c}")
