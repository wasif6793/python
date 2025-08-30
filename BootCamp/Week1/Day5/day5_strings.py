from IPython.extensions.autoreload import update_class

first = 'Hello'
second= "world"

#concatenation
result = first + " "+ second
print(result)

#Slicing
texxt = "My python code"
print(texxt[0:6])
print(texxt[-11:])

#spli()
#join()
#replace()
#strip() - Removes white spaces or specified character from the beginning and the end of the string

print(texxt.split())
print()
texxt2 = "My python code"
sentence = " | ".join(texxt2)
print(sentence)

updates_text = texxt.replace("python","Java")
print(updates_text)

messy_string = "   Hello, World   "
clean_text = messy_string.strip()
print(clean_text)