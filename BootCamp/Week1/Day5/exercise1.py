import re

def clean_text(text):
# remove punctuation
    text = re.sub(r"[^\w\s]","",text)
# Remove extra spaces
    text = " ".join(text.split())
#Convert to lower text
    return text.lower()

input_text = "  Hello, World.!!! Welocme to Python programming..."
cleaned_text = clean_text(input_text)
print(clean_text(input_text))