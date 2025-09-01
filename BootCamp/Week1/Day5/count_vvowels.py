from soupsieve.util import lower


def vowels(string):
    str2 = lower(string)
    ls = list(string)
    count = 0
    for n in ls:
        if n in ["a","e","i","o","u"]:
            count +=1

    return count

strr = input("Enter string: ")
print(vowels(strr))