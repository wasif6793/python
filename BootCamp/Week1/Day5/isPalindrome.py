def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text = input("Enter text:")
if is_palindrome(input_text):
    print("Palindrome")
else:
    print("Not a palindrome")

