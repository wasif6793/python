#Check for prime and composite number
num = int(input("Enter a number: "))

if num <= 1:
    print("Neither prime nor composite")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Composite number")
