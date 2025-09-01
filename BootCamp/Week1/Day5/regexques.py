#Create a program to find and replace all email addresses in a text using regex

import re

text = "Contact us: alice@example.com or bob@domain.org."

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
result = re.sub(pattern, '[email protected]', text)

print(result)