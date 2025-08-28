#Percentage to grades

def convert_to_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

score = int(input("Enter your pecentage: "))
print(f"Your grade is {convert_to_grade(score)}")