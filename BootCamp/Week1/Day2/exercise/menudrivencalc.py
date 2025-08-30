def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if( b != 0):
        return a / b

    else:
        return "DIvision by zero is not allowed"

while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. DIvision")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting Program....")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result: ",add(num1,num2))

    elif choice == '2':
        print("Result: ",sub(num1,num2))
    elif choice == '3':
        print("Result: ", mul(num1, num2))
    elif choice == '4':
        print("Result: ",div(num1,num2))

    else:
        print("Invalid choice.... Please try again.")

