def reverse_string(s):
    chars = list(s)
    for i in range(len(chars) // 2):
        temp = chars[i]
        chars[i] = chars[len(chars) - 1 - i]
        chars[len(chars) - 1 - i] = temp

    return f"Reversed string is {''.join(chars)}"


def count_vowels(s):
    s = s.lower()
    chars = list(s)
    count = 0
    for i in chars:
        if  i in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    return f"Total vowels in {s} is {count}"

def palindrome(s):
    new_s= s.lower()
    chars = list(new_s)

    for i in range(len(chars) // 2):
        if( chars[i] != chars[len(chars) - 1 - i]):
            return f"{s} is not a palindrome"

    return f"{s} is a palindrome"



