
def compute(str):
    char_count = 0
    dig_count = 0
    symb_count = 0

    for char in str:
        if char.isdigit():
            dig_count += 1
        elif char.isalpha():
            char_count += 1
        else:
            symb_count += 1
    print("Digit count: ", dig_count)
    print("Symbol count: ", symb_count)
    print("Character count: ", char_count)

str = "Wasif123 @#$ 10.00.10"
compute(str)

