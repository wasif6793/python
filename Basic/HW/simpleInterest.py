#Calculation for simple interest

principle_amount = int(input("Enter principle amount: "))
rate = int(input("Enter rate of interest per year: "))
time = int(input("Enter time ( in years): "))

SI = (principle_amount * rate * time) / 100

print(f"The simple Interset is {SI}")