#Check number is prime or not from 1 to 100
for num in range(1, 101):
    if num <= 1:
        print(f"{num} is neither prime nor composite")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is a composite number")
